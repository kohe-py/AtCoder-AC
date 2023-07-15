
from collections import deque, defaultdict

string = "snuke"
order = defaultdict(str)
for i in range(5):
    if i <= 3:
        order[string[i]] = string[i + 1]
    else:
        order[string[i]] = string[0]


h, w = map(int, input().split())
G = [input() for _ in range(h)]

            
stack = [(0, 0)]
used = [[False] * w for _ in range(h)]
used[0][0] = True
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while stack:
    i, j = stack.pop()
    now = G[i][j]
    for di, dj in directions:
        ni = i + di
        nj = j + dj
        if ni == -1 or ni == h or nj == -1 or nj == w:
            continue
        if G[ni][nj] not in {"s", "n", "u", "k", "e"} or used[ni][nj]:
            continue
        if G[ni][nj] == order[now]:
            used[ni][nj] = True
            stack.append((ni, nj))
            if ni == h - 1 and nj == w - 1:
                print("Yes")
                exit()
print("No")