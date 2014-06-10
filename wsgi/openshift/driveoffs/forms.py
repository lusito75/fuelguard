from django import forms

from .models import Driveoff

class DriveoffForm(forms.ModelForm):
    class Meta:
        model = Driveoff
