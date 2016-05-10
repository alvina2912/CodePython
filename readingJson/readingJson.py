import urllib
import json
import datetime

today = datetime.date.today()
tomorrow= today+ datetime.timedelta(days=1)
print "tomorrow",tomorrow


dt_txt=str(tomorrow)+" 09:00:00"
print "dt_txt", dt_txt

nextDayURL='http://api.openweathermap.org/data/2.5/forecast?q=mapleGrove%20USA&mode=json&appid=b32debdbdfd202fa62923f26a74459aa'
uh = urllib.urlopen(nextDayURL)
data = uh.read()

try: js = json.loads(str(data))
except: js = None

for i in range (len(js['list'])):

    #print js['list'][i]['dt_txt']
    if dt_txt==js['list'][i]['dt_txt']:
        print js['list'][i]['dt_txt']
        nextDayTemp=js['list'][i]['main']['temp']
        print "nextDayTemp : ",nextDayTemp
        nextDayWeather=js['list'][i]['weather'][0]['main']
        print "nextDayWeather : ",nextDayWeather
        nextDayDescription=js['list'][i]['weather'][0]['description']


print nextDayDescription
print nextDayTemp
