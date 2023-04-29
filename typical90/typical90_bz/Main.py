N, M = map(int, input().split())
g = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

ans = 0
for i in range(N):
    g[i].sort()
    if len(g[i]) >= 2:
        if g[i][0] < i and g[i][1] > i:
            ans += 1
    elif len(g[i]) >= 1:
        if g[i][0] < i:
            ans += 1
    else:
        pass

print(ans)