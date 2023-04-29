from collections import deque
N, Q = map(int, input().split())
g = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

Dist = [10**14 for _ in range(N)]
# 1番(i = 0)の街から各街への距離を求めるBFS
def bfs():
    que = deque()
    que.append(0)
    Dist[0] = 0

    while len(que) != 0:
        p = que.popleft()
        for i in g[p]:
            if Dist[i] == 10**14:
                que.append(i)
                Dist[i] = Dist[p] + 1
    return

bfs()
for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (Dist[c] - Dist[d]) % 2 == 1:
        print("Road")
    else:
        print("Town")