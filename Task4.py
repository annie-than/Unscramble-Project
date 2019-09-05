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

text_sen_list = []
text_rec_list = []
call_cal_list = []
call_rec_list = []

for i in range(len(texts)):
    text_sen_list.append(texts[i][0])
    text_rec_list.append(texts[i][1])
    
for j in range(len(calls)):
    call_cal_list.append(calls[j][0])
    call_rec_list.append(calls[j][1])
    
pos_tele = []
for phone in call_cal_list:
    if phone not in call_rec_list:
        if phone not in text_sen_list:
            if phone not in text_rec_list:
                pos_tele.append(phone)

pos_tele.sort()

postele_list = []
for phone in pos_tele:
    if phone not in postele_list:
        postele_list.append(phone)
        print(phone)
        