
import json
from datetime import datetime

def app(environ, start_response):
    """Simple JSON API"""

    url = environ['RAW_URI']
    time = datetime.now().strftime("%H:%M:%S")
    data = json.dumps({'url': url, 'time': time}, indent=4).encode('utf-8')
    status = '200 OK'
    response_headers = [
        ('Content-type', 'application/json'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])