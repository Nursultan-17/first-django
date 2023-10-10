from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # models.CASCADE - каскадное удаление(Если этот User удалится, то и данный пост тоже удалится)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True - При первом создании поста, выставляется текущая дата. Изменить ее нельзя

class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    in_active = models.BooleanField(True)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()


# Create your models here.
