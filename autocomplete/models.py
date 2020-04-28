from django.db import models

# Create your models here.

class AutoCmplItems(models.Model):
    question = models.CharField("Autocomplete Items")
