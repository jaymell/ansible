#!/usr/bin/python

import redis
import syslog
import time

r = redis.StrictRedis()
p = r.pubsub()
p.psubscribe('rsyslog_*')

syslog.syslog(syslog.LOG_CRIT, "OH FUCK")

# why not:
time.sleep(1)

msg = p.get_message()
while msg:
    # should see "OH FUCK", need to
    # pass random string then attempt
    # to regex it and set exit code
    # accordingly:
    print(msg)
    msg = p.get_message()
