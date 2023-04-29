N = int(input())
result = [0] * (2 * 10 ** 5 + 1)
m = 0
for i in range(N):
    # L以上R未満
    L, R = map(int, input().split())
    m = max(R, m)
    result[L] += 1
    result[R] -= 1
#print(result)
ans = [0]
for i in range(1, m+2):
    ans.append(result[i-1] + ans[i-1])
#print(ans)
flag = 0
S = []
E = []
for i in range(m+2):
    if flag % 2 == 0:
        if ans[i] >= 1:
            flag += 1
            S.append(i-1)
    else:
        if ans[i] == 0:
            flag += 1
            E.append(i-1)

#print(S)
for i in range(len(S)):
    print(S[i], E[i])