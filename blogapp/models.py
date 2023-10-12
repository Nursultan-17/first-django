from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # models.CASCADE - каскадное удаление(Если этот User удалится, то и данный пост тоже удалится)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True - При первом создании поста, выставляется текущая дата. Изменить ее нельзя
    def __str__(self):
        return str(self.title) + ' - ' + str(self.created_at)[:19]

class Story(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    in_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def __str__(self):
        return str(self.author) + ' - ' + str(self.created_at)[:19]

class Flower(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=20)


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    price = models.CharField(max_length=20)


