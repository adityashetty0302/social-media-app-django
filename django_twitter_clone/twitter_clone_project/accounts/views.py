from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreateForm
from django.views.generic import TemplateView


class SignUp(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


class IndexPage(TemplateView):
    template_name = 'index.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'
