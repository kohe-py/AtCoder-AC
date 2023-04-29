import bisect

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
xy.sort(lambda x: (x[0], -x[1]))

L = [5000000] * (N+1)
L[0] = -5000000

ans = 0
for x, y in xy:
    Y = bisect.bisect_left(L, y)
    ans = max(ans, Y)
    L[Y] = y

print(ans)