from rest_framework import viewsets

from oreplay.auth import token_required

from .models import Organizer
from .serializers import OrganizerSerializer


class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = Organizer.objects.active()
    serializer_class = OrganizerSerializer

    @token_required
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @token_required
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @token_required
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
