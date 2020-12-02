from django.forms import ModelForm, DateInput
from django.forms import widgets
from .models import Event
from django import forms

FORMAT_DATE = '%Y-%m-%dT%H:%M'


class EventForm(ModelForm):
    class Meta:
        model = Event
        widgets = {
            'start time': DateInput(attrs={'type': 'datetime-local'}, format=FORMAT_DATE),
            'end date': DateInput(attrs={'type': 'datetime-local'}, format=FORMAT_DATE)
        }
        exclude = ['users']

        def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)
            self.fields['start_time'].input_formats = (FORMAT_DATE)
            self.fields['end_time'].input_formats = (FORMAT_DATE)
