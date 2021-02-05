# secondstring.py
# A program that asks the user to enter a string and prints out 
# every second letter of that string in reverse order
# Author: Fiachra O' Donoghue

# Ask the user to enter a string and assign it to the variable sentence
sentence = input("Please enter a sentence: ")

# take a slice from the string, starting at the end and taking every second character
output = sentence[::-2]

# print the modified string to stdoutx
print(output)