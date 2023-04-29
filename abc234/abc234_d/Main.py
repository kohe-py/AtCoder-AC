import heapq
N, K = map(int, input().split())
P = list(map(int, input().split()))

hq = P[:K]
print(min(hq))
heapq.heapify(hq)
for i in range(N-K):
    x = heapq.heappop(hq)
    heapq.heappush(hq, max(P[K+i], x))
    ans = heapq.heappop(hq)
    print(ans)
    heapq.heappush(hq, ans)