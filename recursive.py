#factorial

def factorial(x):
    """
    Thsi si a recusive function
    to find the factorial of an integers
    """
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))

num=6
print("The factorial of ", num, "is", factorial(num))

#1*2*3*4*5*6=720
factorial(3)--> 1st call with 3
3 * factorial(2) --> 2nd call with 2
3 *2 * factorial(1) --> 3rd call with 1
3*2*1
3*2
6
#stack

