from django.test import TestCase
from django.db import IntegrityError

from lifeflags.flags import models

class FlagUnitTests(TestCase):
    urls = 'lifeflags.flags.urls'

    def create_flag(self, overrides={}, save=True):
        """
        Convience function for creating Flag objects.

        Overrides are merged with sane defaults and 
        applied to the new object.

        The object is saved and it's .id is asserted,
        unless save=False
        """
        defaults = {
            'offense': "Being a free man",
            'players': "Number 6",
            'penalty': "Half the distane to the Village",
        }
        defaults.update(overrides)
        o = models.Flag(**defaults)
        if save:
            o.save()
            self.assert_(o.id)
        return o

    def test_slug_creation(self):
        """
        A flag object should automatically create a 
        TinyURL-esque slug when saved.
        """
        f = self.create_flag(save=False)
        f.save()
        self.assert_(f.slug)

    def test_slug_collision(self):
        """
        If we make 1000 slugs none should collide
        """
        for i in xrange(0,1000):
            f = self.create_flag(save=False)
            try:
                f.save()
            except IntegrityError, e:
                print models.Flag.objects.all().count()
                raise e
                 

    def test_view_show(self):
        """
        /(slug)/ should return a view of the Flag
        """
        f = self.create_flag()

        r = self.client.get('/%s/' % f.slug)

        self.assertEqual(r.status_code, 200)
