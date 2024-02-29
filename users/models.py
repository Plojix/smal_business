from django.db import models

# Create your models here.

class UserModel(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    second_name = models.CharField(max_length=50, null=False)
    phone_number = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=False, unique=True)
    gender = models.CharField(max_length=1, null=False)
    password = models.CharField(max_length=60, null=False)

