#Write a program that prints on the console the first 11 terms of the Fibonacci series (staring from 0)

n = 11
a = 0
b = 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b