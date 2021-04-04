import os
import requests
from flask import Flask, request
import gevent

api_port = os.environ.get('PORT_API', '8000')

app = Flask(__name__)


@app.route('/')
def index():
    
    def foo():
        for i in range(10):
            print(f"foo {i}")
            gevent.sleep(1)

    foos = []
    for i in range(5):
        foos.append(gevent.spawn(foo))
    gevent.joinall(foos)
    return 'Hi there!'