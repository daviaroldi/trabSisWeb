from django.db import models
from .ClientModel import Client

class Proposal(models.Model):

    class Meta:
        db_table = 'proposal'

    title = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, related_name='proposal')
    # client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, related_name='contracts')