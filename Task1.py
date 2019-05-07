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
    
texts_calls = text_sen_list + text_rec_list + call_cal_list + call_rec_list
    
    
texts_calls.sort()

count = len(texts_calls)
for i in range(1, len(texts_calls)):
    if texts_calls[i] == texts_calls[i-1]:
        count -= 1

print("There are {} different telephone numbers in the records.".format(count))