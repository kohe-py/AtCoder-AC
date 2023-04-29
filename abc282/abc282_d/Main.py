from collections import deque, defaultdict
N, M = map(int, input().split())

g = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

#まず二部グラフ判定
seen = [False] * (N)
count = 0
color = [0 for i in range(N+1)]
d = defaultdict(list)
for i in range(N):
    if seen[i]:
        continue
    else:
        count += 1
        d[count] = [1, 1, 0]
        todo = deque([i])
        seen[i], color[i] = True, 1
        while todo:
            v = todo.popleft()
            for j in g[v]:
                if seen[j] == False:
                    todo.append(j)
                    seen[j] = True
                    d[count][0] += 1
                if color[j] == 0:
                    color[j] = color[v] * (-1)
                    d[count][color[j]] += 1
                elif color[j] == color[v]:
                    print(0)
                    exit()
                else:
                    pass


if count == 1:
    print(d[1][1] * d[1][2] - M)

else:
    ans = N * (N - 1) // 2 - M
    for i in range(1, count + 1):
        ans -= (d[i][1] * (d[i][1] - 1) // 2)
        ans -= (d[i][2] * (d[i][2] - 1) // 2)
    print(ans)