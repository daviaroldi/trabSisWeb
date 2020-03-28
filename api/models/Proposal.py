from django.db import models

class Proposal(models.Model):

    class Meta:
        db_table = 'contract'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()
    # album = models.ForeignKey('Album', related_name='musics')

    def __str__(self):
        return self.title