# faships/forms.py
from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Buglist, Tracker

class BuglistForm(forms.ModelForm):
    class Meta:
        model = Buglist
        fields = ('status', 'types', 'title', 'content',)


class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ('buglist', 'message',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['buglist'].queryset = Buglist.objects.filter(status='OPEN')