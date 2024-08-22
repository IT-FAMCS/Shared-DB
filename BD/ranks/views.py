from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Ranks
from .serializer import RankSerializer
from django.urls import reverse_lazy
from rest_framework.response import Response

class RankList(generics.ListAPIView):
    #permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Ranks.objects.all()
    serializer_class = RankSerializer


class RankCreate(mixins.UpdateModelMixin, generics.CreateAPIView):
    #permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Ranks.objects.all()
    serializer_class = RankSerializer
    
class RankUpdateView(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Ranks.objects.all()
    serializer_class = RankSerializer
    
    lookup_field = "role"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)