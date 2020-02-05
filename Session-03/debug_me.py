

def g(a, b):
    return a - b


def f(a, b, c, d):
    t0 = a + b - g(a, 0)
    t1 = g(c, d)
    t3 = 2 * (t0 / t1)
    return t0 + 2*t1 + t3*t3


# -- Main program
print("Result 1: ", f(5, 2, 5, 0))
print("Result 2: ", f(0, 2, 3, 3))
print("Result 3: ", f(1, 3, 2, 3))
print("Result 4: ", f(1, 9, 22.0, 3))

#Execute the program. What happens?
# It gives an error in lines 11 and 17 but it works for the first result

#Execute it step by step. Could you find where is the problem!
# The zero division error happens because when the function is calledin result 2, the calculation for t1 = 0, and when the program continues,
# that zero is dragged untill t3 = 2 * (t0 / t1), which gives an error because of the 0 as the denominator of the division