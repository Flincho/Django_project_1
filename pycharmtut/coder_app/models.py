from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()


class Student(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()


class Professor(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    profession = models.CharField(max_length=40)


class Homework(models.Model):
    name = models.CharField(max_length=40)
    due_date = models.DateField()
    delivered = models.BooleanField()
