from django import forms
from . import models


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("message", "group")
        model = models.Post