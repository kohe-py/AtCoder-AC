N, A, X, Y = map(int, input().split())

ans = 0
for i in range(N):
    if A >= 1:
        ans += X
        A -= 1
    else:
        ans += Y
print(ans)