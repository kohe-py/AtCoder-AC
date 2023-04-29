from collections import deque
N = int(input())
t = []
k = []
A_deq = deque()
for _ in range(N):
    A = deque(map(int, input().split()))
    t.append(A.popleft())
    k.append(A.popleft())
    A_deq.append(A)
ans = 0
Done = [False] * (N+1)
Done[N] = True
still = deque()
still.append(N)
while still:
    v = still.popleft()
    for i in A_deq[v-1]:
        if not Done[i]:
            Done[i] = True
            still.append(i)
for i in range(len(Done)):
    if Done[i]:
        ans += t[i-1]
print(ans)