import numpy
#I am guessing the user might want to use float numbers, so my variables will hold float not intigers.
x=float(input("Please enter 1st number: "))
y=float (input("Please enter 2nd number: "))
print(str(x) + " raised to the power of " + str(y) + " is " + str(x**y))
#I am assigning a variable called edison to hold the answer for log
edison=numpy.log2(x)
print(f"The log base 2 of {x} is: {edison}")