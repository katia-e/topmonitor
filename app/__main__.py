from gevent import monkey
monkey.patch_all()

import os
from gevent.pywsgi import WSGIServer
from app import app

api_port = os.environ.get('PORT_API', '8000')

http_server = WSGIServer(('0.0.0.0', int(api_port)), app)
http_server.serve_forever()