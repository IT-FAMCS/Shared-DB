from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Departs
from .serializer import DepartSerializer
from rest_framework.response import Response

class DepartList(generics.ListAPIView):
    #permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Departs.objects.all()
    serializer_class = DepartSerializer


class DepartCreate(mixins.UpdateModelMixin, generics.CreateAPIView):
    #permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Departs.objects.all()
    serializer_class = DepartSerializer

    
class DepartUpdateView(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Departs.objects.all()
    serializer_class = DepartSerializer
    
    lookup_field = "title"

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