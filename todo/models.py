from django.db import models

# Create your models here.
class TodoGroup(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add= True)
    del_yn = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Todo(models.Model):
    STATUS_LIST=[
        ('Pending', '할일'),
        ('Inprogress', '진행중'),
        ('End', '완료'), 
    ]
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_LIST)
    reg_date = models.DateField(auto_now_add=True)
    end_date= models.DateField(blank=True)
    del_yn = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, upload_to = '%Y/%m')
    group = models.ForeignKey(TodoGroup, models.CASCADE)

class FavouriteGroup(models.Model):
    seq = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Favourite(models.Model):
    seq = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    memo = models.TextField()
    reg_date = models.DateField(auto_now_add = True)
    group = models.ForeignKey(FavouriteGroup, models.CASCADE)