N = int(input())
S = [(input(), _) for _ in range(N)]
S.sort()

ans = [0] * N
def f(x, y):
    result = 0
    for i in range(min(len(x), len(y))):
        if x[i] == y[i]:
            result += 1
        else:
            break
    return result

for i in range(N):
    s, ind = S[i]
    if i != N - 1:
        ans[ind] = f(s, S[i + 1][0])
    if i != 0:
        ans[ind] = max(ans[ind], f(s, S[i - 1][0]))
    
for i in range(N):
    print(ans[i])