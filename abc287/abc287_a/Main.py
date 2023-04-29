N = int(input())
s = [input() for _ in range(N)]

f = 0
a = 0
for i in range(N):
    if s[i] == "For":
        f += 1
    else:
        a += 1

if f > a:
    print("Yes")
else:
    print("No")