from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^send-msg/$', SendMessageAPI.as_view()),
    url(r'^get-msg/$', ReadMessageAPI.as_view()),
]
