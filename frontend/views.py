from __future__ import print_function
# Create your views here.
import os

import firebase_admin
from firebase_admin import messaging, credentials
from django.views.generic import TemplateView

from project.settings import BASE_DIR

creds = credentials.Certificate(os.path.join(BASE_DIR, 'webtechnika.json'))
default_app = firebase_admin.initialize_app(creds)


def send_to_topic():
    topic = 'highScores'

    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        topic=topic,
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        send_to_topic()
        return context