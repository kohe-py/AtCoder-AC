N, K = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    P[i].append(sum(P[i]))
    P[i].append(i)
P.sort(reverse=True, key=lambda x: x[3])
import bisect
ans = [False] * N
border = P[K - 1][3]
for i in range(N):
    if i <= K - 1:
        ans[P[i][4]] = True
    else:
        if P[i][3] + 300 >= border:
            ans[P[i][4]] = True

for i in range(N):
    print("Yes" if ans[i] else "No")
