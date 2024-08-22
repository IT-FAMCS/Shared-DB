from rest_framework import generics, viewsets, mixins
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import User_info
from ranks.models import Ranks
from departs.models import Departs
from users.models import user
from .serializer import UserInfoSerializer
from rest_framework.response import Response

class UserInfoList(generics.ListAPIView):
    #permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = User_info.objects.all()
    serializer_class = UserInfoSerializer


class UserInfoCreate(mixins.UpdateModelMixin, generics.CreateAPIView):
    #permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = User_info.objects.all()
    serializer_class = UserInfoSerializer
    def post(self, request, *args, **kwargs):
        short_title = request.data.get('nickname')
        role = request.data.get('role')
        login = request.data.get('login')
        if User_info.objects.filter(nickname=short_title).exists():
            instance = User_info.objects.get(nickname=short_title)
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            if Ranks.objects.filter(role=role).exists():
                if user.objects.filter(email=login).exists():
                    return self.create(request, *args, **kwargs)
                else:
                    return Response({"error": "No such login in the database."})
            else: 
                return Response({"error": "Role does not exist."})
    
class UserInfoUpdateView(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = User_info.objects.all()
    serializer_class = UserInfoSerializer
    
    lookup_field = "nickname"

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