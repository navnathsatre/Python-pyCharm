import datetime
import time

today = datetime.date.today()
print("Today: ", today)
print("Type of today: ", type(today))

currentTime = datetime.datetime.now()
print("Now: ", currentTime)
print("Type of currentTime: ", type(currentTime))

now = time.time()
print("Now using time module: ", now)

# EPOCH 1970 (Jan 1- 1970)

print("Today            : ", today)
print("Current Time     : ", currentTime)
print("Tuple format     : ", today.timetuple())
print("Ordinal          : ", today.toordinal())
print("Year             : ", today.year)
print("Month            : ", today.month)
print("Day              : ", today.day)