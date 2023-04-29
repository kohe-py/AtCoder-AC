from collections import deque

N, A, B = map(int, input().split())
S = deque(input())

if N == 1:
    print(0)
    exit()
    
ans = 10**18
for i in range(N):
    cand = 0
    for k in range(N//2):
        if S[k] != S[-k-1]:
            cand += B
    ans = min(ans, cand + A * (i))
    S.append(S.popleft())
print(ans)