from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, null=True)
    memo = models.CharField(max_length=300, null=True)
    reg_user = models.ForeignKey(get_user_model(), models.CASCADE)

class Scores(models.Model):
    name = models.CharField(max_length=10)
    math = models.IntegerField()
    english = models.IntegerField()
    science= models.IntegerField()
    reg_date = models.DateField(auto_now_add=True)
    reg_user = models.ForeignKey(get_user_model(), models.CASCADE)

