
# Convert the previous program into the function fibon(n) that calculates the nth Fibonacci term and return it
#The main program should call the fibon() function and print the 5th, 10th and 15th terms in the console

def fibon(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b
    return a

print("The 5th fibonacci term is ", fibon(5))
print("The 10th fibonacci term is", fibon(10))
print("The 15th fibonacci term is ", fibon(15))