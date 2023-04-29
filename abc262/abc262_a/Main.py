y=int(input())
x=y%4
if x <= 2:
    print(y + 2 - x)
elif x == 3:
    print(y + 3)