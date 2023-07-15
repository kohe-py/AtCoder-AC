N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))

from collections import defaultdict
d = defaultdict(int)
for i in range(M):
    d[D[i]] = P[i + 1]

ans = 0
for i in range(N):
    if d[C[i]] == 0:
        ans += P[0]
    else:
        ans += d[C[i]]
print(ans)