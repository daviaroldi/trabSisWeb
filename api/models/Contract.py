from django.db import models
from .proposal import Proposal

class Contract(models.Model):

    class Meta:
        db_table = 'contract'

    title = models.CharField(max_length=200)
    proposal = models.ForeignKey(Proposal, on_delete=models.DO_NOTHING, related_name='musics')