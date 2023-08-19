N = int(input())
xyp = [list(map(int, input().split())) for _ in range(N)]

import math
g = [[0] * N for _ in range(N)]
Max = 0
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        g[i][j] = math.ceil((abs(xyp[i][0] - xyp[j][0]) + abs(xyp[i][1] - xyp[j][1])) / xyp[i][2])
        Max = max(Max, g[i][j])

from collections import deque
ans = 10 ** 18
def cheack(k, s):
    visit = {s}
    todo = deque([s])
    while todo:
        v = todo.popleft()
        for nx in range(N):
            if nx not in visit and g[v][nx] <= k:
                visit.add(nx)
                todo.append(nx)
    if len(visit) == N:
        return True
    else:
        return False
    

def binary_search(s):
    left = 0
    right = Max + 1
    while abs(right - left) > 1:
        center = left + (right - left) // 2
        if cheack(center, s):
            right = center
        else:
            left = center
    return right

ans = 10 ** 18
for i in range(N):
    ans = min(ans, binary_search(i))

print(ans)