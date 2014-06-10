from django.db import models

STATES_AND_TERRITORIES = (
    ('ACT',   'Australian Capital Territory'),
    ('NSW',   'New South Wales'),
    ('NT',    'Northern Territory'),
    ('QLD',   'Queensland'),
    ('SA',    'South Australia'),
    ('TAS',   'Tasmania'),
    ('VIC',   'Victoria'),
    ('WA',    'Western Australia'),
)

#maintain this list in separate file..
VEHICLE_MAKE = (
    ('VW',     'Volkswagen'),
)

class Driveoff(models.Model):
    rego = models.CharField('Registration number', help_text='Licence Plate', max_length=10)
    state = models.CharField(max_length=3, choices=STATES_AND_TERRITORIES, blank=True)
    make = models.CharField(max_length=40, choices=VEHICLE_MAKE, blank=True)
    #model = models.CharField(max_length=40, choices=MODELS)
    colour = models.CharField(max_length=20, blank=True)
    amount = models.DecimalField('Amount Owing', max_digits=5, decimal_places=2)
    site = models.TextField('Site Address')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.rego + " " + self.site
