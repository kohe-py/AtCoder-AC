N, M = map(int, input().split())

from collections import defaultdict, deque
import heapq
into_num = defaultdict(int)
g = [[] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    g[A - 1].append(B - 1)
    into_num[B - 1] += 1

#print(into_num)
def topological_sort(G, into_num):
    #入ってくる有向辺を持たないノードを列挙
    q = []
    heapq.heapify(q)
    for key in range(N):
        if into_num[key]==0:
            heapq.heappush(q, key)
    
    #以下、幅優先探索
    ans = []
    leng = 0
    while leng < N:
        if len(q) == 0:
            print(-1)
            exit()

        v = heapq.heappop(q)
        ans.append(v + 1)
        leng += 1

        for adj in G[v]:
            into_num[adj] -= 1 #入次数を減らす
            if into_num[adj]==0:
                heapq.heappush(q, adj) #入次数が0になったら、キューに入れる
    
    return ans

result = topological_sort(g, into_num)

print(*result)