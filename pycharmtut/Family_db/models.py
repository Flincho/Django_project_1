from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birthday = models.DateField()
    kinship = models.IntegerField()
    icecream_flavor = models.CharField(max_length=40)
