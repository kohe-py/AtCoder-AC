from collections import defaultdict
import bisect
L, N, M = map(int, input().split())

vl = [list(map(int, input().split())) for _ in range(N)]
vl2 = [list(map(int, input().split())) for _ in range(M)]

count = 0
i, j = 0, 0
x, y = 0, 0
while i < N and j < M:
    if vl[i][0] == vl2[j][0]:
        count += min(x + vl[i][1], y + vl2[j][1]) - max(x, y)
    
    if x + vl[i][1] < y + vl2[j][1]:
        x += vl[i][1]
        i += 1
    else:
        y += vl2[j][1]
        j += 1
print(count)