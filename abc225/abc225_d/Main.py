from collections import deque
N, Q = map(int, input().split())
g_f = [-1] * (N+1)
g_b = [-1] * (N+1)
for _ in range(Q):
    q = list(map(int, input().split()))
    n = q[0]
    if n == 1:
        g_f[q[2]] = q[1]
        g_b[q[1]] = q[2]
    
    elif n == 2:
        g_f[q[2]] = -1
        g_b[q[1]] = -1
    
    else:
        ans = deque()
        # 前を見る
        node = q[1]
        ans.appendleft(node)
        while True:
            if g_f[node] == -1:
                break
            node = g_f[node]
            ans.appendleft(node)
        # usiroを見る
        node = q[1]
        while True:
            if g_b[node] == -1:
                break
            node = g_b[node]
            ans.append(node)
        print(len(ans), *ans)
            
            