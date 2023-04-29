from collections import defaultdict
N, Q = map(int, input().split())

d = defaultdict(int)
for i in range(Q):
    a, x = map(int, input().split())
    if a == 1:
        d[x] += 1
    elif a == 2:
        d[x] += 2
    else:
        if d[x] >= 2:
            print("Yes")
        else:
            print("No")