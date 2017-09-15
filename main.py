import json
import httplib2
import logging
from google.appengine.api import memcache
from oauth2client.contrib.appengine import AppAssertionCredentials

from flask import Flask

app = Flask(__name__)

INSTANCE_NAME = 'your_instance_name'
INSTANCE_ZONE = 'your_instance_zone'
PROJECT = 'your_instance_project'



def get_auth():
    credentials = AppAssertionCredentials(scope='https://www.googleapis.com/auth/compute')
    http_auth = credentials.authorize(httplib2.Http(memcache))
    return http_auth

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/vm/start')
def start_vm():
    http = get_auth()
    api_start_uri = 'https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instances/{instance}/start'
    api_start_uri = api_start_uri.format(project=PROJECT, zone=INSTANCE_ZONE, instance=INSTANCE_NAME)
    response, result = http.request(
        uri=api_start_uri,
        method='POST'
        )

    return result, 200, {'Content-Type': 'application/json'}
@app.route('/vm/stop')
def stop_vm():
    http = get_auth()
    api_stop_uri = 'https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instances/{instance}/stop'
    api_stop_uri = api_stop_uri.format(project=PROJECT, zone=INSTANCE_ZONE, instance=INSTANCE_NAME)
    response, result = http.request(
        uri=api_stop_uri,
        method='POST'
        )

    return result, 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run()
