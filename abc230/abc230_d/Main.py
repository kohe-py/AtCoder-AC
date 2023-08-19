N, D = map(int, input().split())
LD = [list(map(int, input().split())) for _ in range(N)]

LD.sort(key=lambda x: x[1])
now = LD[0][1]
ans = 1
for i in range(1, N):
    if LD[i][0] > now + D - 1:
        ans += 1
        now = LD[i][1]
    else:
        pass
print(ans)
