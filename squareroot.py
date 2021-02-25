# squareroot.py
# Estimate the square root of the provided number
# Author: Fiachra O' Donoghue

# https://www2.math.upenn.edu/~kazdan/202F09/sqrt.pdf
# To approximate the square root, x, of a real number A, we need to solve 
# x**2 - A = 0
# So given a real number A, we estimate the square root, x and calculate x**2 - A
# If the result is greater than 0 then our estimate must be too high, 
# and if it is less than 0 then our estimate must be too low
# If it is too high e should half it and try again, and if it is too low we should
# increase to half way between the current estimate and the last one


def sqrt(a):

    # The first estimate should be such that its square is greater than a
    # https://www2.math.upenn.edu/~kazdan/202F09/sqrt.pdf
    estimate = 0
    
    if a > 1:
        estimate = a / 2

    result = a

    # We must use the absolute result as sometimes the result of x**2 - a < 0 
    while abs(result) > 0.0000000001:

        result = estimate**2 - a

        estimate = (estimate + (a/estimate))/2
 
        print("Result: {}\tEstimate: {}".format(result, estimate))

    return(estimate)
    
#for i in range(100):
print(sqrt(2))
