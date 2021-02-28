# es.py
# Count the number of e's in a passed file
# Author: Fiachra O' Donoghue

# Must import sys to use argv, an array containing 
# the filename and arguments passed to the program
import sys

print(sys.argv[1])

# The first argument passed to the script will be used
file = open(sys.argv[1])

# Declare variable to keep count of e's
count = 0

# Iterate through lines in file
for line in file:

    # For each line iterate through each character
    for character in line:

        # Test if the current character is an 'e'
        if character =='e':
            # ... and if so increment the count
            count += 1

# Print out the number of e's found
print("Count:", count)