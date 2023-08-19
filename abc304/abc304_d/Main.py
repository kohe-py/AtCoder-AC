W, H = map(int, input().split())
N = int(input())
pq = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))

import bisect
from collections import defaultdict
li = defaultdict(int)

for i in range(N):
    x = bisect.bisect_left(a, pq[i][0])
    y = bisect.bisect_left(b, pq[i][1])
    li[f"{x, y}"] += 1

m, M = 10 ** 18, 0
count = 0
for key in li.keys():
    m = min(m, li[key])
    M = max(M, li[key])
    count += 1

if count < (A + 1) * (B + 1):
    m = 0

print(m, M)