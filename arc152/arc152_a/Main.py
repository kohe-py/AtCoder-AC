N, L = map(int, input().split())
a = list(map(int, input().split()))
if L <= 2:
    print("Yes")
    exit()
if a.count(2) == 0:
    print("Yes")
    exit()


count = 0
c = 0
x = a.count(2)
for i in range(N):
    if count == x:
        break
    c += (a[i]+1)
    if a[i] == 2:
        count += 1


if L - c >= -1:
    print("Yes")
else:
    print("No")