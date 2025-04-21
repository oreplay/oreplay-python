from rest_framework import viewsets
from .models import Organizer
from .serializers import OrganizerSerializer


class OrganizerViewSet(viewsets.ModelViewSet):
    queryset = Organizer.objects.filter(deleted__isnull=True)
    serializer_class = OrganizerSerializer
