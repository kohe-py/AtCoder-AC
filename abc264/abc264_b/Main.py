R, C = map(int, input().split())

a = abs(R-8)
b = abs(C-8)
if max(a,b) % 2 == 1:
    print("black")
else:
    print("white")