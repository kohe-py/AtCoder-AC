from collections import defaultdict,deque
import heapq

Q = int(input())
S = defaultdict(int)
max_s = []
min_s = []


for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        S[q[1]] += 1
        heapq.heappush(min_s, q[1])
        heapq.heappush(max_s, -q[1])
            
    elif q[0] == 2:
        S[q[1]] -= min(q[2], S[q[1]])

    else:
        while S[-max_s[0]] == 0:
            heapq.heappop(max_s)
        while S[min_s[0]] == 0:
            heapq.heappop(min_s)
        print(-max_s[0]-min_s[0])