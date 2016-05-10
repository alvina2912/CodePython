import datetime
import time

today = datetime.date.today()
print 'Today    :', today

tomorrow= today+ datetime.timedelta(days=1)

print "Tomorrow  :", tomorrow
