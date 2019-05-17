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
    timeRecord = {}
    for call in calls:
        seconds = int(call[3])
        if call[0] not in timeRecord:
            timeRecord[call[0]] = seconds
        else:
            timeRecord[call[0]] += seconds
        if call[1] not in timeRecord:
            timeRecord[call[1]] = seconds
        else:
            timeRecord[call[1]] += seconds
        
    
    longestTimeRecord = None
    for k, v in timeRecord.items():
        if longestTimeRecord is None:
            longestTimeRecord = (k,v)
        currentCallTime = int(v)
        longestCallTime = int(longestTimeRecord[1])
        if currentCallTime > longestCallTime:
            longestTimeRecord = (k,v)
    return longestTimeRecord

longestCall = longestCall()
print("%s spent the longest time, %d seconds, on the phone during September 2016." % (longestCall[0], longestCall[1]))