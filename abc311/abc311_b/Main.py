N, D = map(int, input().split())
S = [input() for i in range(N)]

ans = [0]
for j in range(D):
    count = 0
    for i in range(N):
        if S[i][j] == "x":
            ans.append(0)
            break
        else:
            count += 1
    if count == N:
        ans[-1] += 1

#print(ans)
print(max(ans))