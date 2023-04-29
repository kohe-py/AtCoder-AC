import math
R, X, Y = map(int, input().split())

dist = math.sqrt((X)**2 + (Y)**2)
ans = (-dist // R)
if dist < R:
    print(2)
    exit()
print(int(-ans))