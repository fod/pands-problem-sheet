# collatz.py
# Perform a series of calculations on a user input positive integer:
# 1. If number is even, divide by 2; if number is odd multiply by 3 and add 1
# 2. Repeat until number is 1
# Author: Fiachra O' Donoghue

# Request user input and cast input as an integer
num = int(input("Please enter a positive integer: "))

# Print a newline to improve readability of output
print("\n")

# Print the provided number as specified in the problem output example
# The end argument to the print statement places a space instead of a carriage return after 
# each printed number so that they all appear on the same line
print(num, end = " ")

# While loop runs until 'num' reaches 1
while (num != 1):

    # if num % 2 = 0 then num is even as it is divisible by 2...
    if (num % 2 == 0):

        # ...so num is divided by 2. Integer divison (//) is used so that a float is not returned.
        # This does not affect the value of the result because the number is even and will therefore 
        # be divisible by 2 but it prevents the numbers being printed with a '.0' appended
        num //= 2
        
    else:

        # Otherwise number must be odd and so is multiplied by 3 and 1 is added as specified
        num = (num * 3) + 1
    
    # Print out the value of num at the end of each iteration of the while loop
    print(num, end = " ")

# Some newlines to improve output readability in the terminal
print("\n\n")

