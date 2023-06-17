N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

import bisect


B.sort()

ans = -1
for i in range(N):
    x = A[i]
    y = A[i] + D
    ind_x = bisect.bisect_right(B, x)
    ind_y = bisect.bisect_right(B, y)
    if abs(A[i] - B[ind_x - 1]) <= D:
        ans = max(ans, A[i] + B[ind_x - 1])
    if abs(A[i] - B[ind_y - 1]) <= D:
        ans = max(ans, A[i] + B[ind_y - 1])

print(ans)