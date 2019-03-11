import os

import firebase_admin
from django.core.management.base import BaseCommand
from firebase_admin import credentials, messaging

from project.settings import BASE_DIR

creds = credentials.Certificate(os.path.join(BASE_DIR, 'webtechnika.json'))
default_app = firebase_admin.initialize_app(creds)


def send_to_token():
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        token='f1TbiTptFfk:APA91bGEyE-aIXaX2A-aOXmgT8syfJJFTVHE0ZuZAzE9xsJYXVltNcKrHIPKkijODGrKXVlueEuIqTHwD1uSKU6kFc0hY-pKxAb_LFgk9_fUT6DhIeUrUhE4ONQ6qOmWMLIeEMgNApsa'
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)


class Command(BaseCommand):
    help = 'Send example message to FireBase app'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        send_to_token()