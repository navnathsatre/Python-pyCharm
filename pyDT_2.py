import datetime

print("microseconds         : ", datetime.timedelta(microseconds=1))
print("milliseconds         : ", datetime.timedelta(milliseconds=1))
print("seconds              : ", datetime.timedelta(seconds=1))
print("minutes              : ", datetime.timedelta(minutes=1))
print("hours                : ", datetime.timedelta(hours=1))
print("days                 : ", datetime.timedelta(days=1))
print("weeks                : ", datetime.timedelta(weeks=1))


# today = datetime.date.today()
today = datetime.datetime.now()

print("Today                : ", today)

delta = datetime.timedelta(days=7, hours=4, minutes=10, seconds=40)

yday = today - delta
tom  = today + delta

print("Yesterday            : ", yday)
print("Tommorow             : ", tom)