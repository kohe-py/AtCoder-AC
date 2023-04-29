import itertools
N, M = map(int, input().split())

t = [[False] * N for _ in range(N)]
a = [[False] * N for _ in range(N)]



for _ in range(M):
    A, B = map(int, input().split())
    t[A-1][B-1] = True
    t[B-1][A-1] = True
    
for _ in range(M):
    C, D = map(int, input().split())
    a[C-1][D-1] = True
    a[D-1][C-1] = True
    
ans = False

for p in itertools.permutations(range(N)):
    #print(p)
    ok = True
    for i in range(N):
        for j in range(N):
            if t[i][j] != a[p[i]][p[j]]:
                ok = False
    if ok:
        ans = True
print("Yes" if ans else "No")