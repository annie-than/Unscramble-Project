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

phone_dic = {}

for call in calls:
    calling = call[0]
    receiving = call[1]
    calltime = int(call[3])
    
    phone_dic.setdefault(calling, 0)
    phone_dic[calling] = phone_dic[calling] + calltime
    phone_dic.setdefault(receiving, 0)
    phone_dic[receiving] = phone_dic[receiving] + calltime

phone_num = max(phone_dic.items(), key = lambda x: x[1] )

print("{} spent the longest time, {}, one the phone during September 2016".format(phone_num[0], phone_num[1]))

