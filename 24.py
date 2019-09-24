import datetime
import pytz
import calendar


d = datetime.date(2016, 7, 24)
print(d)
tday = datetime.date.today()
print(tday)
print(tday.day)
print(tday.weekday())
print(tday.isoweekday())
print(tday.year)
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)
print(tday - 8 * tdelta)
print(tdelta)
bday = datetime.date(2020, 9, 17)
till_bday = bday - tday
print(till_bday.total_seconds())
t = datetime.time(9, 30, 45, 100000)
print(t)
print(t.hour)
dt = datetime.datetime.today()
print(dt)
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)
dt_utcnow = datetime.datetime.utcnow()
print(dt_utcnow)
dt_mtz = dt_utcnow.astimezone(pytz.timezone('Europe/Paris'))
print(dt_mtz)
print(pytz.all_timezones_set)
for tz in sorted(pytz.all_timezones_set):
    print(tz)
print(dt_utcnow.isoformat())
print(dt_mtz.weekday())
print(calendar.day_name[dt_mtz.weekday()])
"""strftime - datetime to string"""
print(dt_mtz.strftime('%B %d, %Y'))
"""strptime - string to datetime"""
dt_str = 'September 24, 2019'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)
