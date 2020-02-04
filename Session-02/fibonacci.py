#Write a program that prints on the console the first 11 terms of the Fibonacci series (staring from 0)


a = 0
b = 1

for i in range(n):
    c = b + a
    a = b
    b = c

print(a)