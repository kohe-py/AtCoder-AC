import heapq
N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
from collections import deque
ans = []
s = set()
todo = [0]

heapq.heapify(todo)
count = 0
while True:
    v = heapq.heappop(todo)
    ans.append(v)
    count += 1
    if count == K + 1:
        break
    for i in A:
        if v + i not in s:
            s.add(v+i)
            heapq.heappush(todo, v + i)
#print(ans)
print(ans[K])