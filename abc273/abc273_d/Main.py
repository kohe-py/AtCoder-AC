H, W, r, c = map(int, input().split())
N = int(input())
rc = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())

from collections import defaultdict
import bisect
yoko = defaultdict(list)
tate = defaultdict(list)

for i in range(N):
    x, y = rc[i][0], rc[i][1]
    yoko[x].append(y)
    tate[y].append(x)
    
for i in yoko.keys():
    yoko[i].sort()
for i in tate.keys():
    tate[i].sort()

now = [r, c]
for _ in range(Q):
    x, y = now[0], now[1]
    d, l = map(str, input().split())
    l = int(l)
    if d == "L":
        ind = bisect.bisect_left(yoko[x], y)
        if ind == 0:
            now[1] = max(1, now[1] - l)
        else:
            now[1] = max(now[1] - l, yoko[x][ind - 1] + 1)
    elif d == "R":
        ind = bisect.bisect_left(yoko[x], y)
        leng = len(yoko[x])
        if ind == leng:
            now[1] = min(W, now[1] + l)
        else:
            now[1] = min(now[1] + l, yoko[x][ind] - 1)
    elif d == "U":
        ind = bisect.bisect_left(tate[y], x)
        if ind == 0:
            now[0] = max(1, now[0] - l)
        else:
            now[0] = max(now[0] - l, tate[y][ind - 1] + 1)

    else:
        ind = bisect.bisect_left(tate[y], x)
        leng = len(tate[y])
        if ind == leng:
            now[0] = min(H, now[0] + l)
        else:
            now[0] = min(now[0] + l, tate[y][ind] - 1)
    print(*now)