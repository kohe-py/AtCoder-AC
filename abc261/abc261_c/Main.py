N = int(input())
S = [input() for _ in range(N)]

p=dict()
for i in range(N):
    p[S[i]] = 0

for i in range(N):
    if p[S[i]] >= 1:
        print(S[i] + "({})".format(p[S[i]]))
    else:
        print(S[i])
    p[S[i]] += 1