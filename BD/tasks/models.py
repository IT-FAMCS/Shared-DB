from django.db import models

class Tasks(models.Model):
    nickname = models.CharField(max_length=150)
    task = models.CharField(max_length=150)
    descr = models.CharField(max_length=1000)
    department = models.CharField(max_length=150, default="Общая")
    deadline = models.CharField(max_length=150)