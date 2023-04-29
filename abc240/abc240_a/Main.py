a, b = map(int, input().split())

if a == b + 1 or a + 1 == b:
    print("Yes")
    exit()
if (a == 10 and b == 1) or (b == 10 and a == 1):
    print("Yes")
    exit()
print("No")