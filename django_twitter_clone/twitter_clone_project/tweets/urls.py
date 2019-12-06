from django.urls import path
from . import views

app_name = 'tweets'

urlpatterns = [
    path('new/', CreateTweet.as_view(), name='new')
]
