
# Models sind ind DJango die Datenbanken basierend auf SQLite3

from django.db import models

class Kommentare(models.Model):
  player = models.CharField(max_length=255)
  comment = models.CharField(max_length=500)

  def __str__(self):
    return self.comment