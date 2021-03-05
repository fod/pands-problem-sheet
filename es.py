# es.py
# Count the number of e's in a passed file
# Author: Fiachra O' Donoghue

# Must import sys to use argv, an array containing 
# the filename and arguments passed to the program
import sys

# The first argument passed to the script is stored as the
# second element in the sys.argv list
filename = sys.argv[1]

# Open file in read mode ('r') using the with keyword so that resources
# are automatically releases when the file read is complete
with open (filename, 'r') as file:

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