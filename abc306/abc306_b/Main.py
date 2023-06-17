A = list(map(int, input().split()))

ans = 0
tow = 1
for i in range(64):
    if A[i] == 1:
        ans += A[i] * tow
    tow *= 2

print(ans)