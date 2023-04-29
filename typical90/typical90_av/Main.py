from collections import deque
N, K = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
a = [0] * N
b = [0] * N
for i in range(N):
    a[i] = (ab[i][0] - ab[i][1])
    b[i] = ab[i][1]

ans = 0
a.sort()
b.sort()

while True:
    if K <= 0:
        break
    K -= 1
    if len(b) >= 1:
        if a[-1] <= b[-1]:
            ans += b[-1]
            b.pop()
        else:
            ans += a.pop()
    else:
        ans += a.pop()
print(ans)