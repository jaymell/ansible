#!/usr/bin/python

import redis
import syslog
import time
import sys

r = redis.StrictRedis()
p = r.pubsub()
p.psubscribe('rsyslog_*')
MESSAGE = 'OH FUCK'
syslog.syslog(syslog.LOG_CRIT, MESSAGE)

# why not:
time.sleep(1)

msg = p.get_message()
while msg:
	if msg['data']:
		if isinstance(msg['data'], basestring):
		    if MESSAGE in msg['data']:
		    	sys.exit(0)
	msg = p.get_message()

sys.exit(1)
