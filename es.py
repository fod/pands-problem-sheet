# es.py
# Count the number of e's in a passed file
# Author: Fiachra O' Donoghue

import sys

print(sys.argv[1])

file = open(sys.argv[1])

print(file)

count = 0
for line in file:
    for character in line:
        if character =='e':
            count += 1

print("Count:", count)