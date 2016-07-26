# faships/forms.py
from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Buglist, Tracker, Station


BuglistFormSet = inlineformset_factory(
    Buglist, Station, extra=0, min_num=1,
    fields=('stationid', 'status',)
)


class BuglistForm(forms.ModelForm):
    class Meta:
        model = Buglist
        fields = ('status', 'types', 'station', 'content',)


class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ('buglist', 'message',)
        widgets = {'buglist': forms.HiddenInput}

    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['buglist'].queryset = Buglist.objects.filter(status='OPEN')

    def __init__(self, *args, submit_title='Submit', **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', submit_title))