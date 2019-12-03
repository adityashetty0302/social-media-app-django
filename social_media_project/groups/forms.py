from django import forms
from . import models


class GroupForm(forms.ModelForm):
    class Meta:
        fields = ("name", "description")
        model = models.Group
