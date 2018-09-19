#!/usr/bin/python 
import urllib2
import json
import base64
import sys
# first argument should be ip address
# second argument should be port
# third argument should be one of queue names
# fourth argument should be 'EnqueueCount or 'DequeueCount' or 'ConsumerCounts or 'OueueSize'
base64string = base64.encodestring('%s:%s' % ('USER', 'PASSWORD')).replace('\n','')
url = littp://{0}:{1}/api/jolokia/read/org.apache.activemq:brokerName=localhost,destinationName={2},destinationType=gueue,type=Broker.format(sys.argv[1], sys.argv[2], sys.argv[3])
request = ur11ib2.Request(url)

request.add_header("Authorization", "Basic %s" % base64string)

result = urllib2.urlopen(request)
data = result.read() 
r = json.loads(data) 
print int(r['valu']['{}'.format(sys.argv[4])])

