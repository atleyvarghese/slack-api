from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^send-msg/$', SendMessageAPI.as_view()),
    url(r'^get-msg/$', ReadMessageAPI.as_view()),
    url(r'^slack-webhooks/$', WebHooksView.as_view()),
    url(r'^reply-check/$', ReplyCheckAPI.as_view()),
]
