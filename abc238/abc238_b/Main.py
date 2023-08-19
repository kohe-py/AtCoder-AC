N = int(input())
A = list(map(int, input().split()))

cut = [False] * 360
cut[0] = True
s = 0

for i in range(N):
    s = (s + A[i]) % 360
    cut[s] = True

ans, tmp = 0, 1
for i in range(360):
    if cut[i]:
        ans = max(ans, tmp)
        tmp = 1
    else:
        tmp += 1
ans = max(ans, tmp)
print(ans)