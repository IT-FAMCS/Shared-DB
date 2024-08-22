from django.db import models

class Ranks(models.Model):
    role = models.CharField(max_length=30, unique=True)