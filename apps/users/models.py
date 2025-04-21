from django.db import models
from django.utils.timezone import now


class User(models.Model):
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

    def delete(self, using=None, keep_parents=False):
        self.deleted = now()
        self.save()

    objects = models.Manager()

    class Meta:
        db_table = "users"


class AccessToken(models.Model):
    access_token = models.CharField(max_length=40, primary_key=True)
    client_id = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    expires = models.DateTimeField()
    scope = models.CharField(max_length=2000, null=True, blank=True)

    objects = models.Manager()

    class Meta:
        db_table = "oauth_access_tokens"
