from django.db import models
from django.contrib.auth.models import User
from countries.models import Country
from datetime import datetime
# Create your models here.
def now():
    return datetime.now()
class Person(User):
    name = models.CharField(max_length=500)
    city = models.CharField(max_length=280, blank=True)
    country = models.ForeignKey(Country)
    postal = models.CharField(max_length=255,blank=True)
    phone = models.PositiveIntegerField()
    emergency_contact = models.PositiveIntegerField()

    def __unicode__(self):
        return unicode(self.name)