from datetime import date, time, datetime, timedelta
import datetime

date_0 = date(year=2021, month=2, day=3)
date_1 = date.today()
date_2 = date_1.replace(month=1)
print(date_2)
print(date_2.ctime())

time_1 = time(hour=1)
time_2 = time_1.replace(microsecond=123456)


print(time_2)

dt_1 = datetime(year=2021, month=2, day=3, hour=1, minute=34)
dt_2 = datetime.combine(date=date_2, time=time_2)
print(dt_2.ctime())
print(dt_2)

# %d - Day
# %m - Month
# %y, %Y - Year
# %H - hour
# %M - minutes
# %S - seconds
print(dt_2.strftime('%S:%M:%H %d-%m-%y'))
print(dt_2.strftime('%S:%M:%H %d-%m-%Y'))

delta = dt_1 - dt_2
delta_1 = timedelta(hours=1, minutes=5, seconds=12, weeks=3, milliseconds=123)
print(dt_2)
print(dt_1)
print(delta_1)