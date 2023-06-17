N, M = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(M)]
from collections import defaultdict

d = defaultdict(set)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i != j:
            d[i].add(j)

for i in range(M):
    for j in range(N - 1):
        d[a[i][j]].discard(a[i][j + 1])
        d[a[i][j + 1]].discard(a[i][j])

count = 0
for i in range(1, N + 1):
    count += len(d[i])

print(count // 2)