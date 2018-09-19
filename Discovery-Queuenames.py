#!/usr/bin/python2.7
import sys
import requests
import json
# first argument should be ip address
# second argument should be port
def jsonparser():
   data = []
   result = json.loads(r.content)
   for item in result['value'].keys():
       qnames = item.split(",")[1].split("=")[1]
       data.append('{#01NAME}':quames})
       return json.dumps({"data":data})

urll = http://{}:{}/api/jolokia/read/org.apache.activemq:brokerName=localhost,destinationName=*,destinationType=Queue,type=Broker.format(sys.argv[1], sys.argv[2]) 
try:
   r = requests.get(url=urll, auth=('USERNAME', 'PASSWORD')
   print(jsonparser()) 
except ValueError as a:
   print a
