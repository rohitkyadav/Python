import datetime

today = datetime.date.today()
print(today.day)
print(today.strftime("today's date is %d %b %Y"))
print(today.strftime("today's date is %d %m %y"))

todaytime = datetime.datetime.now()
print(todaytime.minute)