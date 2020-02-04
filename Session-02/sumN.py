#.. 1 +  2 + + 3 +  ... + 20
# ..1 + ... + 100


def sum(n):
    res = 0
    for i in range(1, n+1):
        res += 1
    return res



print("sum of 1-20: ", sum(20))
print("sum of 1-100: ", sum(100))
