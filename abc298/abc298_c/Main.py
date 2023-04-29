import bisect
from collections import defaultdict
N = int(input())
Q = int(input())
hako = defaultdict(list)
kado = defaultdict(list)
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        i = q[1]
        j = q[2]
        hako[j].append(i)
        kado[i].append(j)
    elif q[0] == 2:
        i = q[1]
        hako[i].sort()
        print(*hako[i])
    else:
        i = q[1]
        kado[i].sort()
        print(*set(kado[i]))