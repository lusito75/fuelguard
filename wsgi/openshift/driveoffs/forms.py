from django import forms
from django.forms.widgets import TextInput

from .models import Driveoff

class DriveoffForm(forms.ModelForm):
    class Meta:
        model = Driveoff


class RegoSearchForm(forms.ModelForm):
    class Meta:
        model = Driveoff
        widgets = {
            'rego': forms.TextInput(attrs={}),
            'colour': forms.TextInput(attrs={}),
        }
        fields = ['rego', 'colour', 'make', 'model', ]
