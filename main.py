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
    return ''.join([x['name'] for x in instances)
def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items']

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/a')
def hello_world_info():
    return get_all(), 200
                    
#@app.route('/vm/start')
#def start_vm():
#    compute = get_auth()
#    api_start_uri = 'https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instances/{instance}/start'
#    api_start_uri = api_start_uri.format(project=PROJECT, zone=INSTANCE_ZONE, instance=INSTANCE_NAME)
#    response, result = http.request(
#        uri=api_start_uri,
#        method='POST'
#       )

#    return result, 200, {'Content-Type': 'application/json'}
#@app.route('/vm/stop')
#def stop_vm():
#    http = get_auth()
#    api_stop_uri = 'https://www.googleapis.com/compute/v1/projects/{project}/zones/{zone}/instances/{instance}/stop'
#    api_stop_uri = api_stop_uri.format(project=PROJECT, zone=INSTANCE_ZONE, instance=INSTANCE_NAME)
#    response, result = http.request(
#        uri=api_stop_uri,
#        method='POST'
#        )

#    return result, 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run()
