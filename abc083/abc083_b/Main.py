N, A, B = map(int, input().split())
ans = 0
for i in range(N+1):
    x=0
    for j in str(i):
        x += int(j)
    if A <= x <= B:
        ans += int(i)
print(ans)