N = int(input())
A, B, C = map(int, input().split())

ans = 9999
for i in range(10**4):
    for j in range(10**4):
        k = (N - A*i - B*j)
        if k % C == 0 and k >= 0:
            ans = min(ans, (k // C) + j + i)
print(ans)