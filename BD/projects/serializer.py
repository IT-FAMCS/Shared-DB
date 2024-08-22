from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

    def create(self, validated_data):
        project_name = validated_data.get('title')

        try:
            project = Project.objects.get(title=project_name)
            for key, value in validated_data.items():
                setattr(project, key, value)
            project.save()

        except Project.DoesNotExist:
            project = Project.objects.create(**validated_data)

        return project

    def update(self, instance, validated_data):

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
