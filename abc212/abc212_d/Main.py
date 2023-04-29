import heapq 

Q = int(input())
result=[]
heapq.heapify(result) 
count = 0
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        heapq.heappush(result, q[1]- count)
    elif q[0] == 2:
        count += q[1]
    else:
        x = heapq.heappop(result)
        print(x + count)