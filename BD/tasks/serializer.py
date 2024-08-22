from rest_framework import serializers
from .models import Tasks


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = '__all__'

    def create(self, validated_data):
        task_name = validated_data.get('task')

        try:
            task = Tasks.objects.get(task=task_name)
            for key, value in validated_data.items():
                setattr(task, key, value)
            task.save()

        except Tasks.DoesNotExist:
            task = Tasks.objects.create(**validated_data)

        return task

    def update(self, instance, validated_data):

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
