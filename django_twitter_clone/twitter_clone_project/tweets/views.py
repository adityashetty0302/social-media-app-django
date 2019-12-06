from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from . import forms
from . import models

class CreateTweet(LoginRequiredMixin, generic.CreateView):
    fields = ('tweet',)
    model = models.Tweets

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)