from django.db import models

# Create your models here.
class Hobby(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    imageLink = models.CharField(max_length=500, default='https://static.thenounproject.com/png/583402-200.png')

    def __str__(self):
        return (self.name + ": " + self.description + "\n")

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    imageLink = models.CharField(max_length=500, default='https://static.thenounproject.com/png/583402-200.png')

    def __str__(self):
        return (self.name + ": " + self.description + "\n")