import math
L = int(input())
def combinations_count(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))
x = combinations_count(L-1, 11)
print(x)