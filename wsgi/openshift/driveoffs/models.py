from django.db import models

STATES_AND_TERRITORIES = (
    ('ACT',   'ACT'),
    ('NSW',   'NSW'),
    ('NT',    'NT'),
    ('QLD',   'QLD'),
    ('SA',    'SA'),
    ('TAS',   'TAS'),
    ('VIC',   'VIC'),
    ('WA',    'WA'),
)

#maintain this list in separate file..
VEHICLE_MAKE = (
    ('VW',     'Volkswagen'),
)

class Driveoff(models.Model):
    rego = models.CharField(help_text='(excluding any \'-\')', max_length=10)
    state = models.CharField(max_length=3, choices=STATES_AND_TERRITORIES, blank=True)
    #make = models.CharField(max_length=40, choices=VEHICLE_MAKE, blank=True)
    make = models.CharField(max_length=40, blank=True)
    model = models.CharField(max_length=40, blank=True)
    colour = models.CharField(max_length=20, blank=True)
    amount = models.DecimalField('Amount Owing', max_digits=5, decimal_places=2)
    site = models.TextField('Site Address')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.rego + "   " + self.site
