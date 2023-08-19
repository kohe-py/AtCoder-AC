N = int(input())
fs = [list(map(int, input().split())) for _ in range(N)]

fs.sort(key = lambda x: x[1], reverse=True)
if fs[0][0] != fs[1][0]:
    print(fs[0][1] + fs[1][1])
    exit()

ans = fs[0][1] + (fs[1][1] // 2)
for i in range(N):
    if fs[i][0] != fs[0][0]:
        print(max(ans, fs[0][1] + fs[i][1]))
        exit()
print(ans)
