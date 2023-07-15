N, K = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N)]

ab = sorted(ab, key=lambda x:x[0])
#print(ab)
s = 0
for i in range(N):
    s += ab[i][1]

ans = 1

if s <= K:
    print(ans)
    exit()


for i in range(N):
    s -= ab[i][1]
    if i < N - 1:
        ans = ab[i][0]
    elif i == N - 1:
        ans = ab[i][0]

    if s <= K:
        break

print(ans + 1)