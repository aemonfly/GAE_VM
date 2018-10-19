import json
import logging
from google.appengine.api import memcache
from oauth2client.client import GoogleCredentials
from googleapiclient import discovery
from flask import Flask
app = Flask(__name__)
INSTANCE_NAME = 'instance-1'
INSTANCE_ZONE = 'asia-east1-a'
PROJECT = 'mm-7713'
COMPUTE = discovery.build(
    'compute', 'v1', credentials=GoogleCredentials.get_application_default())
def get_all():
    instances = list_instances(COMPUTE,PROJECT,INSTANCE_ZONE)
    return ''.join(str(e) for e in instances)
def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items']
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/a')
def hello_world_info():
    return get_all(), 200
@app.route('/start')
def hello_start():
    return str(COMPUTE.instances().start(project=PROJECT, zone=INSTANCE_ZONE, instance=INSTANCE_NAME).execute()), 200
@app.route('/stop')
def hello_stop():
    return str(COMPUTE.instances().stop(project=PROJECT, zone=INSTANCE_ZONE, instance=INSTANCE_NAME).execute()), 200
if __name__ == '__main__':
    app.run()
