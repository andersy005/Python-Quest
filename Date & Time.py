import time
import calendar

ticks = time.time()
print(ticks)

localtime = time.localtime(time.time())
print("Local Current time : ", localtime)

# Formatted Time

localtime = time.asctime(time.localtime(time.time()))
print("Local Current time : ", localtime)

# Getting Calendar

cal = calendar.month(2016,1)
print('Here is the calendar : ')
print(cal)