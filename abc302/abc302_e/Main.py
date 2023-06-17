N, Q = map(int, input().split())

flag = [True] * N
from collections import defaultdict
d = defaultdict(set)
ans = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        if len(d[q[1] - 1]) == 0:
            ans += 1
        if len(d[q[2] - 1]) == 0:
            ans += 1
        d[q[1] - 1].add(q[2] - 1)
        d[q[2] - 1].add(q[1] - 1)
        print(N - ans)
    else:
        if len(d[q[1] - 1]) == 0:
            ans += 1
        for v in d[q[1] - 1]:
            d[v].remove(q[1] - 1)
            if len(d[v]) == 0:
                ans -= 1
        d[q[1] - 1] = set()
        ans -= 1
        print(N - ans)