#!/usr/bin/python2.7
import requests
import json
import sys

# first argument should be IP 
# second argument should be PORT

def jsonparser():
    result = json.loads(r.content)
    time = str(result['value']['Uptime']).split(" ")
    if len(time) == 4 and int(time[0]) >= 24 and int(time[2]) > 10:
        return "ERROR"
    else:
        return "OK"
urll = 'http://{}:{}/api/jolokia/read/org.apache.activemq:brokerName=localhost,type=Broker'.format(sys.argv[1], sys.argv[2])
try:
    r = requests.get(url=urll, auth=('admin', '@ctiveMQ'))
    print(jsonparser())
except ValueError as a:
    print(a)
