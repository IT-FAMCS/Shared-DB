from django.db import models

class Departs(models.Model):
    title = models.CharField(max_length=150, unique=True)