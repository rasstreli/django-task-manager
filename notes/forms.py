__author__ = 'pavel'
from django import forms
from notes.models import Jobs
from persons.models import Person
class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs

class UpdateJobForm(forms.Form):
    title = forms.CharField(max_length=240, widget=forms.TextInput(attrs={'class':'input-xlarge'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'input-xxlarge'}))
    author = forms.ModelChoiceField(Person.objects.all())