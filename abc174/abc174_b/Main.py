N, D = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(N)]

count = 0
for i in range(N):
    if xy[i][0] ** 2 + xy[i][1] **2 <= D**2:
        count += 1
print(count)