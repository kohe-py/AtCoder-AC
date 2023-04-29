from collections import Counter
N, K = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
for bit in range(1 << N):
    count = [0] * 26
    for i in range(N):
        if bit >> i & 1:
            for j in range(len(S[i])):
                count[ord(S[i][j]) - ord("a")] += 1
    c = 0
    for k in range(26):
        if count[k] == K:
            c += 1
    ans = max(ans, c)
print(ans)