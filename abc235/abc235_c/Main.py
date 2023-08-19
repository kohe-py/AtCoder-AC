N, Q = map(int, input().split())
a = list(map(int, input().split()))

from collections import Counter, defaultdict
d = defaultdict(list)
counter = Counter(a)

for i in range(N):
    d[a[i]].append(i + 1)

for _ in range(Q):
    x, k = map(int, input().split())
    if counter[x] < k:
        print(-1)
    else:
        print(d[x][k - 1])
