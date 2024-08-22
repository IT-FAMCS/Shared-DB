from rest_framework import serializers
from .models import User_info

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_info
        fields = '__all__'

    def create(self, validated_data):
        user_info_name = validated_data.get('nickname')

        try:
            user_info = User_info.objects.get(nickname=user_info_name)
            for key, value in validated_data.items():
                setattr(user_info, key, value)
            user_info.save()

        except User_info.DoesNotExist:
            user_info = User_info.objects.create(**validated_data)
                
        return user_info

    def update(self, instance, validated_data):
        
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()


        return instance