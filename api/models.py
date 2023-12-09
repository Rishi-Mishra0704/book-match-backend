# models.py
from django.db import models

class Student(models.Model):
    name = models.CharField( max_length=100)
    fiction_score = models.IntegerField()
    non_fiction_score = models.IntegerField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    fiction_score = models.IntegerField()
    non_fiction_score = models.IntegerField()

    def __str__(self):
        return self.title