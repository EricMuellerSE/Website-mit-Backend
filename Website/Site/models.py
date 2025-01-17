from django.db import models

class Kommentare(models.Model):
  player = models.CharField(max_length=255)
  comment = models.CharField(max_length=500)
  active = True