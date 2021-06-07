
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
import requests
import json

from django.conf import settings


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--lat',
            dest='lat',
            default=0,
            help='Latitude')

        parser.add_argument('--long',
            dest='long',
            default=0,
            help='Longitude')

        parser.add_argument('--content',
            dest='content',
            default='',
            help='Content')

    def handle(self, *args, **options):
        command = {
            "method": "publish",
            "params": {
                "channel": "public:map",
                "data": {
                    "lat": options.get("lat"),
                    "long": options.get("long"),
                    "content": options.get("content")  
                }
            }
        }

        api_key = settings.CENTRIFUGO_API_KEY
        data = json.dumps(command)
        headers = {'Content-type': 'application/json', 'Authorization': 'apikey ' + api_key}
        resp = requests.post("http://localhost:8081/api", data=data, headers=headers)
