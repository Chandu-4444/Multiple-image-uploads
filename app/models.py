from django.db import models

class MultipleImage(models.Model):
    images = models.FileField()