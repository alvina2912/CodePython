import calendar

print calendar.TextCalendar(firstweekday=6).formatyear(2016)

m,d,y=map(int,raw_input().split())
print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())
