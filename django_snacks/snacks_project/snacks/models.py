from pyexpat import model
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

class Snack (models.Model):
    name=models.TextField(max_length=255)

    def __str__(self) :
        return self.name