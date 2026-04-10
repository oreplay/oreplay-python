from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import check_password as django_check_password
from django.contrib.auth.hashers import make_password
from django.db import models
from django.utils.crypto import salted_hmac
from django.utils.timezone import now

try:
    import bcrypt
except ImportError:  # pragma: no cover - dependency is installed in Docker
    bcrypt = None


class UserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The email field is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_super", True)
        return self.create_user(email, password, **extra_fields)


class User(models.Model):
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    id = models.CharField(max_length=36, primary_key=True)
    email = models.EmailField(max_length=160, unique=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_super = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    def delete(self, using=None, keep_parents=False):
        self.deleted = now()
        self.save()

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email

    def get_username(self):
        return self.email

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        if not self.password or raw_password is None:
            return False

        if self.password.startswith("$2y$") or self.password.startswith("$2b$"):
            if bcrypt is None:
                return False
            encoded_password = self.password.replace("$2y$", "$2b$", 1).encode("utf-8")
            return bcrypt.checkpw(raw_password.encode("utf-8"), encoded_password)

        return django_check_password(raw_password, self.password)

    def get_session_auth_hash(self):
        return salted_hmac(
            f"{self.__class__.__module__}.{self.__class__.__name__}",
            self.password or "",
        ).hexdigest()

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def is_active(self):
        return self.deleted is None

    @property
    def username(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_super

    def has_perm(self, perm, obj=None):
        return bool(self.is_admin or self.is_super)

    def has_perms(self, perm_list, obj=None):
        return all(self.has_perm(perm, obj=obj) for perm in perm_list)

    def has_module_perms(self, app_label):
        return bool(self.is_admin or self.is_super)


class AccessToken(models.Model):
    access_token = models.CharField(max_length=40, primary_key=True)
    client_id = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    expires = models.DateTimeField()
    scope = models.CharField(max_length=2000, null=True, blank=True)

    objects = models.Manager()

    class Meta:
        db_table = "oauth_access_tokens"
