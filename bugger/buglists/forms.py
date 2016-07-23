# faships/forms.py
from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Buglist

class BuglistForm(forms.ModelForm):
    class Meta:
        model = Buglist
        fields = ('title', 'content',)