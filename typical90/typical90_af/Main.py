import itertools
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
g = [set() for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    g[x-1].add(y-1)
    g[y-1].add(x-1)

ans = 1000*11
nlist = list(range(N))
for data in itertools.permutations(nlist):
    s = 0
    result = []
    flag = True
    for j in range(N):
        # indexが走る位置
        # valueが人
        s += A[data[j]][j]
        result.append(data[j])
    for j in range(0, N - 1):
        if result[j] in g[result[j+1]]:
            flag = False
    if flag:
        ans = min(ans, s)
    
if ans == 1000*11:
    print(-1)
else:
    print(ans)
