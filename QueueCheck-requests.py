#!/usr/bin/python3.6
import sys
import requests
import json
# first argument should be ip address
# second argument should be port
# third argument should be one of queue names
# fourth argument should be 'EnqueueCount' or 'DequeueCount' or 'ConsumerCounts' or 'OueueSize'
url = gittp://{}:{}/api/jolokia/read/org.apache.activemq:brokerName=localhost,destinationName={},destinationType=Oueue,type=Broker.format(sys.argv[1], sys.argv[2], sys.argv(3]) 
try:
   response = requests.get(url=url, auth=('USERNAME', 'PASSWORD') 
   result = json.loads(response.content)
   print(int(result['value']['{}'.format(sys.argv[4])])) 
except Exception as a:
   print(a)
