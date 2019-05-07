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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

texts_inc = texts[0][0]
texts_ans = texts[0][1]
texts_time = texts[0][2]
calls_inc = calls[-1][0]
calls_ans = calls[-1][1]
calls_time = calls[-1][2]
calls_last = calls[-1][3]

print("First record of texts, {} texts {} at time {}".format(texts_inc, texts_ans, texts_time))
print("Last record of calls, %s calls %s at time %s, lasting %s seconds" %(calls_inc, calls_ans, calls_time, calls_last))