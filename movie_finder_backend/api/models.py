from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=19)

class Manager(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=19)

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.TextField()
    text = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    publisher = models.ForeignKey(Manager, on_delete=models.CASCADE, blank=True, null=True)