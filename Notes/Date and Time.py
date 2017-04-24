from datetime import datetime
now = datetime.now()

print "The hour:minute:second\n" + '%s:%s:%s' % (now.hour, now.minute, now.second)
print "The month/day/year\n" + "%s/%s/%s" %(now.month, now.day, now.year)
