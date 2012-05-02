__author__ = 'pavel'
from django.contrib import admin
from notes.models import Notes, Actions, Jobs, DurationTypes, Status

admin.site.register(Notes)
admin.site.register(Jobs)
admin.site.register(Actions)
admin.site.register(DurationTypes)
admin.site.register(Status)