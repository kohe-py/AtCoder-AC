N, K = map(int, input().split())
A = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(N)]

m = []
for j in range(N):
    x = xy[j][0]
    y = xy[j][1]
    n = 10 ** 18
    for i in range(K):
        a = xy[A[i] - 1][0]
        b = xy[A[i] - 1][1]
        R = (x - a) ** 2 + (y - b) ** 2
        if n >= R:
            n = R
    m.append(n)

print(max(m)**0.5)   