N, M = map(int, input().split())

dist = [[10 ** 18] * N for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    dist[A - 1][B - 1] = C
for i in range(N):
    dist[i][i] = 0

ans = 0
for k in range(N):
    nxt = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            nxt[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            if nxt[i][j] != 10 ** 18:
                ans += nxt[i][j]
    dist = nxt
print(ans)