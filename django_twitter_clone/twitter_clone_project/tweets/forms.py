from django import forms
from . import models


class TweetsForm(forms.ModelForm):
    class Meta:
        fields = ("tweet",)
        model = models.Tweets
