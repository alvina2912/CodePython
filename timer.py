from threading import Timer
import datetime

def task():
    print "I am running at " , datetime.datetime.now()
    t1 = Timer(1,task)
    t1.start()

t = Timer(1 , task)
t.start()
