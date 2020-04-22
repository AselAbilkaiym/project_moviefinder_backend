from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.TextField()
    text = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)