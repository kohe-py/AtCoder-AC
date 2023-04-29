N, M = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        count = 0
        if i == j:
            break
        for k in range(M):
            if S[i][k] == "o" or S[j][k] == "o":
                count += 1
        
            else:
                break
        if count == M:
            ans += 1
print(ans)