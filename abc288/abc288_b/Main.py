N, K = map(int, input().split())
s = [input() for _ in range(N)]

ans = []
for i in range(K):
    ans.append(s[i])
ans.sort()
for i in range(K):
    print(ans[i])