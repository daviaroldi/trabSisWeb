from django.db import models
from .ClientModel import Client

class Document(models.Model):

    class Meta:
        db_table = 'document'

    name = models.CharField(max_length=200)
    path = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, related_name='document')