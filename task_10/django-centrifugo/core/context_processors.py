
import jwt

from django.conf import settings


def main(request):
    return dict(
        CENTRIFUGE_SOCKJS_ENDPOINT=settings.CENTRIFUGE_ADDRESS + '/connection/sockjs',
        CENTRIFUGE_WS_ENDPOINT=settings.CENTRIFUGE_ADDRESS + '/connection/websocket',
        CENTRIFUGE_TOKEN=jwt.encode({"sub": ""}, settings.CENTRIFUGE_SECRET),
    )
