from django.db import models

class User_info(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    fathername = models.CharField(max_length=150)
    birthdate = models.CharField(max_length=150)
    role = models.CharField(max_length=150, default="Работяга1")
    login = models.CharField(max_length=150, unique = True)
    nickname = models.CharField(max_length=150, default="", unique = True)  
    pension = models.BooleanField(default=False)
    
class Departments(models.Model):
    event = models.ForeignKey(User_info, related_name='departments', on_delete=models.CASCADE)
    title = models.TextField()