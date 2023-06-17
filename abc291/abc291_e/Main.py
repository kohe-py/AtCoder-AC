N, M = map(int, input().split())
g = [set() for _ in range(N)]
G = [set() for _ in range(N)]
for _ in range(M):
    X, Y = map(int, input().split())
    g[X - 1].add(Y - 1)
    G[Y - 1].add(X - 1)

from collections import deque
def topological_sort(G, into_num):
    #入ってくる有向辺を持たないノードを列挙
    q = deque()
    #V: 頂点数
    for i in range(N):
        if into_num[i]==0:
            q.append(i)
    
    #以下、幅優先探索
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1 #入次数を減らす
            if into_num[adj]==0:
                q.append(adj) #入次数が0になったら、キューに入れる
    
    return ans
into_num = [0] * N
for i in range(N):
    into_num[i] = len(G[i])

result = topological_sort(g, into_num)
if result == []:
    print("No")
    exit()

for i in range(N - 1):
    if result[i + 1] not in g[result[i]]:
        print("No")
        exit()

print("Yes")
ans = [0] * N
for i in range(N):
    ans[result[i]] = i + 1
print(*ans)