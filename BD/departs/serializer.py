from rest_framework import serializers
from .models import Departs

class DepartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departs
        fields = '__all__'

    def create(self, validated_data):
        depart_name = validated_data.get('title')

        try:
            depart = Departs.objects.get(title=depart_name)
            for key, value in validated_data.items():
                setattr(depart, key, value)
            depart.save()

        except Departs.DoesNotExist:
            depart = Departs.objects.create(**validated_data)
                
        return depart

    def update(self, instance, validated_data):
        
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()


        return instance