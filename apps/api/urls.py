from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^send-msg/$', SendMessageAPIView.as_view(), name='upc-scan'),
    url(r'^get-msg/$', ReadMessageAPIView.as_view(), name='get-msgs'),
    url(r'^slack-webhooks/$', WebHooksView.as_view(), name='webhooks'),
    url(r'^reply-check/$', ReplyCheckAPIView.as_view(), name='replies'),
]
