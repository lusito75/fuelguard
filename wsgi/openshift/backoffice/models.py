from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class CustomerProfile(models.Model):
    user          = models.OneToOneField(User, unique=True, verbose_name=('user'), related_name='profile')
    customer_name = models.CharField(max_length=128, unique=True, db_index=True)
    site_address  = models.TextField('Site Address', blank=False)
    phone         = models.CharField('Phone number', help_text='Including area code', max_length=32, blank=True)

    def __unicode__(self):
        return "%s's Profile" % (self.customer_name or self.user)


class Subscription(models.Model):
    plan = models.CharField(max_length=60)
    customer = models.ForeignKey('CustomerProfile')
    last_updated = models.DateTimeField(auto_now=True)
    expiration = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.plan
