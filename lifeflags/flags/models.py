import random, time

from django.db import models

from shorturls.baseconv import base62

class Flag(models.Model):
    """
    Represents a 'flag on the play'.
    Flag on the play. {{ Offense }}, {{ players }}. {{ Penalty }}
    """
    slug = models.SlugField(unique=True, max_length=50, null=True)
    offense = models.CharField(max_length=140)
    players = models.CharField(max_length=140)
    penalty = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s-%s - %s, %s." % (self.id, self.slug, self.offense, self.players)

    def save(self, force_insert=False, force_update=False):
        super(Flag, self).save(force_insert, force_update)
        if not self.slug:
            self.slug = "F%s" % hash(self.id)
            super(Flag, self).save(force_insert, force_update)

    @models.permalink
    def get_absolute_url(self):
        return ('detail_view', (), {'slug': self.slug})
