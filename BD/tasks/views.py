from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Tasks
from users_info.models import User_info
from .serializer import TaskSerializer
from rest_framework.response import Response


class taskList(generics.ListAPIView):
    #permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer


class taskCreate(mixins.UpdateModelMixin, generics.CreateAPIView):
    #permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    
    def post(self, request, *args, **kwargs):
        nickname = request.data.get('nickname')
        if User_info.objects.filter(nickname=nickname).exists():
            return self.create(request, *args, **kwargs)
        else:
            return Response({"error": "Nickname does not exist."})


class taskUpdateView(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    lookup_field = "task"

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
