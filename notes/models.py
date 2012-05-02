from django.db import models
from persons.models import Person
from datetime import datetime
# Create your models here.

def now():
    return datetime.now()

class Jobs(models.Model):
    status = models.ForeignKey("Status")
    responsible = models.ForeignKey(Person, related_name='owned_issued')
    author = models.ForeignKey(Person, related_name='issue_author')
    description = models.TextField()
    start_date = models.DateTimeField(default= now())
    end_date = models.DateTimeField(default=now())
    work_units = models.FloatField()
    action = models.ForeignKey('Actions')

    class Meta:
        verbose_name_plural = "Jobs"

    def __unicode__(self):
        return unicode(self.responsible)

class Notes(models.Model):
    eb = models.ForeignKey(Person)
    description = models.TextField()
    duration = models.TimeField(default=now())
    timestamp = models.DateTimeField(default=now())
    duration_type = models.ForeignKey('DurationTypes')

    class Meta:
        verbose_name_plural = "Notes"

class Status(models.Model):
    name = models.CharField(max_length= 150)

    class Meta:
        verbose_name_plural = "Statuses"

    def __unicode__(self):
       return  self.name

class Actions(models.Model):
    name = models.CharField(max_length=600)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Actions"

    def __unicode__(self):
        return self.name

class DurationTypes(models.Model):
    type = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Duration Types"

    def __unicode__(self):
        return self.type