import heapq
from collections import deque

li = []
A = deque()
Q = int(input())

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        A.append(q[1])
    elif q[0] == 2:
        if len(li) != 0:
            ans = heapq.heappop(li)
            print(ans)
        else:
            print(A.popleft())
    else:
        for i in A:
            heapq.heappush(li, i)
        A = deque()