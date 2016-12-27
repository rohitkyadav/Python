import datetime

today = str(datetime.date.today())
print(today)
print(today.strftime("today's date is %d %b %Y"))
print(today.strftime("today's date is %d %m %y"))

todaytime = datetime.datetime.now()
print(todaytime.minute)