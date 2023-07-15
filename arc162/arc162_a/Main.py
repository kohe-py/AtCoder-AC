T = int(input())
from collections import defaultdict
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    ind = defaultdict(int)
    for i in range(N):
        ind[P[i]] = i
    now = ind[1]
    ans = 1
    for i in range(2, N + 1):
        if now < ind[i]:
            ans += 1
            now = ind[i]
    print(ans)