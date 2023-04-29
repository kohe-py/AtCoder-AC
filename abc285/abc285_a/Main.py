a,b = map(int, input().split())

if a > b:
    if a == 2*b or a == 2*b + 1:
        print("Yes")
    else:
        print("No")
else:
    if b == 2*a + 1 or b == 2*a:
        print("Yes")
    else:
        print("No")