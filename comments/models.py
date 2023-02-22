from django.db import models


class UserComment(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    comment = models.CharField(max_length=1000)