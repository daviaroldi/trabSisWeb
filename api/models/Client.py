from django.db import models
from .proposal import Proposal

class Client(models.Model):

    class Meta:
        db_table = 'client'

    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)
    proposals = models.ForeignKey(Proposal, on_delete=models.DO_NOTHING, related_name='client')
    