# Time Conversion
import sys
time = raw_input().strip()

hour=int(time[0:2])
min=int(time[3:5])
sec=int(time[6:8])
timeOfDay=time[9:]

if hour==12 and timeOfDay=='am' :
    hour=0
elif hour<12 and timeOfDay=='pm' : 
    hour=hour+12
result=str(hour)+":"+str(min)+":"+str(sec)+":"+timeOfDay
#time[0:2]=hour
print result