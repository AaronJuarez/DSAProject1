"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from datetime import datetime

def longestCall():
    longestTimeRecord = calls[0]
    for call in calls:
        currentCallTime = int(call[3])
        longestCallTime = int(longestTimeRecord[3])
        if currentCallTime > longestCallTime:
            longestTimeRecord = call
    return longestTimeRecord

longestCall = longestCall()
callDate = datetime.strptime(longestCall[2], '%d-%m-%Y %H:%M:%S')
print("%s spent the longest time, %s seconds, on the phone during %s" % (longestCall[0], longestCall[3], callDate.strftime('%B %Y')) )