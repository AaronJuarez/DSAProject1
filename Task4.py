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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def discardNumbers():
    discardedNumbers = set()
    for text in texts:
        discardedNumbers.add(text[0])
        discardedNumbers.add(text[1])
    for call in calls:
        discardedNumbers.add(call[1])
    return discardedNumbers

def identifyTelemarketPhone():
    discardedNumbers = discardNumbers()
    possibleNumbers = set()
    for call in calls:
        callingPhone = call[0]
        if callingPhone not in discardedNumbers:
            possibleNumbers.add(callingPhone)

    return sorted(possibleNumbers)

print("These numbers could be telemarketers: \n%s" % ('\n'.join(identifyTelemarketPhone())))

#Simplified version
check_list = set([item[0] for item in texts] + [item[1] for item in texts] + [item[1] for item in calls])

possible_list = set([item[0] for item in calls])
final_list = possible_list - check_list
print("These numbers could be telemarketers:  \n" + "\n".join(sorted(final_list)))