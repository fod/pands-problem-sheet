# squareroot.py
# Estimate the square root of the provided number
# Author: Fiachra O' Donoghue

# This program uses Newton's method to approximate square roots
# The description of Newton's method in the paper below was used to develop the program
# https://www2.math.upenn.edu/~kazdan/202F09/sqrt.pdf

# To approximate the square root, x, of a real number A, we need to solve 
# x**2 - A = 0
# So given a real number A, we estimate the square root, x and calculate (x**2 - A)
# If the result is 0 then we have found the square root
# If the result is not 0 nor within an accptable margin of error from zero then a new 
# and better estimate can be calculated as:
# new_x = (x + (A / x)) / 2  
# (remember that x is the current estimate and A is the number for which the square root 
# is sought)


# The sqrt function takes a number for which the square root will be estimated
# and an optional error limit at which it will stop seeking a better estimate
# The limit defaults to 0.0000000001. This was chosen arbitrarily but tested with
# a wide variety of input data
def sqrt(num, limit = 0.0000000001):

    # The first estimate should be such that its square is greater than A
    # (see https://www2.math.upenn.edu/~kazdan/202F09/sqrt.pdf)

    # If the A is less than 1 then 1 is a good first estimate
    # because its square guaranteed to be bigger than A
    estimate = 1
    
    # and if A is greater than 1 than A/2 is a good first estimate because, again
    # its square is guaranteed to be bigger than A
    if num > 1:
        estimate = num / 2

    # error is the variable that will hold the result of the test calculation
    # (x**2 - A) on each iteration. It must be declared outside the loop as 
    # it provides the stopping condition for the while loop
    error = num

    # We must use the absolute error as sometimes (x**2 - a) < 0 
    while abs(error) > limit:

        # Test the current estimate
        error = estimate**2 - num

        # Calculate the new estimate
        estimate = (estimate + (num / estimate)) / 2

    # Return the approximated square root
    return(estimate)
    
# Obtain number from user
num = float(input("Please enter a positive number: "))

# Approximate the square root
result = sqrt(num)

# Print the result, rounded to 1 decimal place
print("The square root of {} is approx. {:.1f}".format(num, result))