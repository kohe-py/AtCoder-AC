N = int(input())
a = [input() for _ in range(N)]

M = 0
for i, j in zip([0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]):
    for x in range(N):
        for y in range(N):
            dp = ""
            dp += a[x][y]
            for k in range(N-1):
                x += i
                x %= N
                y += j
                y %= N
                dp += a[x][y]
                M = max(M, int(dp))

print(M)