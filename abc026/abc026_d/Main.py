import math

A, B, C = map(int, input().split())

def f(t):
    return A*t + B*math.sin(C*t*math.pi)
t = -1
left = 0
right = 200
while abs(f(t)-100) > 10**(-9):
    t = (left + right) / 2
    if f(t) > 100:
        right = t
    else:
        left = t

print(t)