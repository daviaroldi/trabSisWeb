from django.db import models
from django.contrib.auth.models import User

class Proposal(models.Model):

    class Meta:
        db_table = 'proposal'

    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='proposal')