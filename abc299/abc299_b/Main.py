N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

ans = 0
result = 0
if T in set(C):
    for i in range(N):
        if C[i] == T and result < R[i]:
            ans = i + 1
            result = R[i]
    print(ans)
    exit()
else:
    ans = 1
    result = R[0]
    color = C[0]
    for i in range(N):
        if C[i] == color and result < R[i]:
            ans = i + 1
            result = R[i]
    print(ans)
    exit()