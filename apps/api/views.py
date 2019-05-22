from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests, json
# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from slack_api_test import settings


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class SendMessageAPI(generic.View):

    def post(self, request, *args, **kwargs):
        msg = request.POST.get('message')
        if msg:
            header = {"Authorization": "Bearer " + settings.SLACK_API_TOKEN}
            response = requests.post("https://slack.com/api/chat.postMessage", headers=header,
                                     data={"channel": "#random", "text": msg, "as_user": True})

            messages.success(request, "Msg send")
        else:
            messages.error(request, "Please try agin")
        return redirect('/')

@method_decorator(csrf_exempt, name='dispatch')
class WebHooksView(generic.View):

    def post(self, request, *args, **kwargs):
        return HttpResponse(request.POST.get('challenge'))


class ReadMessageAPI(generic.TemplateView):
    template_name = 'home_1.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        auth_token = "xoxp-642574269621-644436553927-642635455136-6062a5438595576fb24258e0791a37f9"
        header = {"Authorization": "Bearer " + auth_token}
        response = requests.post("https://slack.com/api/channels.history", headers=header,
                             data={"channel": "#random", "count": 10})
        messages.success(self.request, "Msg send")
        return context
