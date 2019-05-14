"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def differentPhones():
    differentPhonesSet = set()
    for row in texts:
        i = 0
        while i in range(2):
            phone = row[i]
            differentPhonesSet.add(phone)
            i += 1
    for row in calls:
        i = 0
        while i in range(2):
            phone = row[i]
            differentPhonesSet.add(phone)
            i += 1
    return len(differentPhonesSet)

print("There are %d different telephone numbers in the records." % (differentPhones()))