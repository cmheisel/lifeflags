import random, time

from django.db import models

from shorturls.baseconv import base62

class Flag(models.Model):
    """
    Represents a 'flag on the play'.
    Flag on the play. {{ Offense }}, {{ players }}. {{ Penalty }}
    """
    slug = models.SlugField(unique=True, max_length=50)
    offense = models.CharField(max_length=140)
    players = models.CharField(max_length=140)
    penalty = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s - %s, %s." % (self.id, self.offense, self.players)

    def __slug_seed(self):
        """
        Return a semi-reliably random and non-repetitive integer
        """
        seed = random.randint(1,10000) + int(time.time()) #Random number + time as int
        return base62.from_decimal(seed)


    def save(self, force_insert=False, force_update=False):
        if not self.slug:
            self.slug = "F%s" % self.__slug_seed() 
        super(Flag, self).save(force_insert, force_update)

