import math 
W, H = map(int, input().split())

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
base = comb(W+H-2, H-1)
print(base%1000000007)