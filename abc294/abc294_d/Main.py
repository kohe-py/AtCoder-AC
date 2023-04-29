from collections import deque, defaultdict
import heapq
N, Q = map(int, input().split())

un_call = []
un_recep = [] 

for i in range(N):
    un_call.append(i+1)

heapq.heapify(un_call)
heapq.heapify(un_recep)
recep = set()

for _ in range(Q):
    #print(un_call, un_recep, recep)
    q = list(map(int, input().split()))
    if q[0] == 1:
        if len(un_call) != 0:
            x = heapq.heappop(un_call)
            heapq.heappush(un_recep, x)
    elif q[0] == 2:
        recep.add(q[1])
    else:
        while un_recep[0] in recep:
            x = heapq.heappop(un_recep)
        print(un_recep[0])