from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter


    def perfom_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            if self.request.user.is_superuser:
                return []
            else:
                return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = (Advertisement.objects.filter(creator=self.request.user) |
                        Advertisement.objects.filter(status='OPEN')) #  queryset_1 | queryset_2
            return queryset
        return super().get_queryset().filter(status='OPEN')
