from django.test import TestCase

from lifeflags.flags import models

class FlagUnitTests(TestCase):
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
