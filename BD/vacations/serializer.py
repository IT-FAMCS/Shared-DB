from rest_framework import serializers
from .models import Vacations


class vacationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacations
        fields = '__all__'

    def create(self, validated_data):
        vacations_name = validated_data.get('short_title')

        try:
            vacations = Vacations.objects.get(short_title=vacations_name)
            for key, value in validated_data.items():
                setattr(vacations, key, value)
            vacations.save()

        except Vacations.DoesNotExist:
            vacations = Vacations.objects.create(**validated_data)

        return vacations

    def update(self, instance, validated_data):

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
