from collections import defaultdict

N, K  = map(int, input().split())
c = list(map(int, input().split()))

d = dict()
s = set()
for i in range(K):
    if c[i] in d:
        d[c[i]] += 1
    else:
        d[c[i]] = 1

ans = len(d)
for i in range(N-K):
    d[c[i]] -= 1
    if c[i+K] in d:
        d[c[i+K]] += 1
    else:
        d[c[i+K]] = 1
    if d[c[i]] == 0:
        d.pop(c[i])
    ans = max(ans, len(d))
    #print(ans)
print(ans)