# secondstring.py
# A program that asks the user to enter a string and prints out 
# every second letter of that string in reverse order
# Author: Fiachra O' Donoghue

# Ask the user to enter a string and assign it to the variable sentence
sentence = input("Please enter a sentence: ")

# Take a slice from the string, starting at the end and taking every second character.
# The empty space before the first colon indicates that the slice should start at 
# the beginning of the string, the empty space before the second colon indicates that the 
# slice should run to the end of the string, the third argument is the step: the fact that 
# it is negative indicates that the slice should start at the end of the string and run 
# backwards through the string, and the 2 indicates that every second character should be 
# included
output = sentence[::-2]

# print the modified string to stdout
print(output)
