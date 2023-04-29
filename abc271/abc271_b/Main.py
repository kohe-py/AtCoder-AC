N,Q=map(int,input().split())
la=[list(map(int,input().split())) for _ in range(N)]


for i in range(Q):
    s, t = map(int, input().split())
    print(la[s-1][t])