import json
import requests
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from slack_api_test import settings

header = {"Authorization": "Bearer " + settings.SLACK_TOKEN}


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class SendMessageAPIView(generic.View):

    def post(self, request, *args, **kwargs):
        msg = request.POST.get('message')
        if msg:
            response = requests.post("https://slack.com/api/chat.postMessage", headers=header,
                                     data={"channel": "#random", "text": msg, "as_user": True})

            request.session['msg_id'] = json.loads(response.content.decode('utf8').replace("'", '"'))["ts"]
            request.session['channel_id'] = json.loads(response.content.decode('utf8').replace("'", '"'))["channel"]

            messages.success(request, "Msg send successfully")
        else:
            messages.error(request, "Please try again later")
        return redirect(reverse('slack:home'))


@method_decorator(csrf_exempt, name='dispatch')
class WebHooksView(generic.View):

    def post(self, request, *args, **kwargs):
        return JsonResponse(data={"challenge": json.loads(request.body.decode('utf8').replace("'", '"'))["challenge"]})


class ReadMessageAPIView(generic.TemplateView):
    template_name = 'data.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.session.get('channel_id'):
            response = requests.post("https://slack.com/api/channels.history", headers=header,
                                     data={"channel": self.request.session.get('channel_id'), "count": 10})
            context['data'] = json.loads(response.content.decode('utf8').replace("'", '"'))['messages']
        return context


class ReplyCheckAPIView(generic.TemplateView):
    template_name = 'data.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.session.get('channel_id'):
            response = requests.post("https://slack.com/api/channels.replies", headers=header,
                                     data={"channel": self.request.session.get('channel_id'),
                                           "thread_ts": self.request.session['msg_id']})
            if len(json.loads(response.content.decode('utf8').replace("'", '"'))['messages']) > 1:
                context['data'] = json.loads(response.content.decode('utf8').replace("'", '"'))['messages']
        return context
