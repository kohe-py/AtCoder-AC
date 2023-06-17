N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict
d = defaultdict(int)
count = defaultdict(int)
for i in range(N):
    d[A[i] + i] += 1
    count[i - A[i]] += 1

ans = 0
for key in d.keys():
    ans += (d[key] * count[key])

print(ans)