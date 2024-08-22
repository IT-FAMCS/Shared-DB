from rest_framework import serializers
from .models import Ranks

class RankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ranks
        fields = '__all__'

    def create(self, validated_data):
        ranks_name = validated_data.get('role')

        try:
            ranks = Ranks.objects.get(role=ranks_name)
            for key, value in validated_data.items():
                setattr(ranks, key, value)
            ranks.save()

        except Ranks.DoesNotExist:
            ranks = Ranks.objects.create(**validated_data)
                
        return ranks

    def update(self, instance, validated_data):
        
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()


        return instance