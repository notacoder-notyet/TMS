from django.utils import timezone
from rest_framework import viewsets

from .models import GlobalTask, Objectives
from .serializers import GlobalTaskSerializer, ObjectivesSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


class GlobalTaskViewSet(viewsets.ModelViewSet):
    queryset = GlobalTask.objects.all()
    serializer_class = GlobalTaskSerializer
    permission_classes = (IsAdminOrReadOnly, )

    def get_queryset(self):
        date = timezone.localdate()
        return super().get_queryset().filter(deadline__gte=date)


class ObjectivesViewSet(viewsets.ModelViewSet):
    # queryset = Objectives.objects.all()
    serializer_class = ObjectivesSerializer
    # permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        date = timezone.localdate()
        return super().get_queryset().filter(deadline__gte=date)