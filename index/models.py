from django.db import models


class Admin(models.Model):
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Themes(models.Model):
    theme = models.CharField(max_length=255)


class Statuses(models.Model):
    status = models.CharField(max_length=255)


class Requests(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE)
    description = models.CharField(max_length=1023)
    date = models.DateTimeField()
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE)


class Codes(models.Model):
    phone = models.CharField(max_length=255)
    code = models.CharField(max_length=4)

