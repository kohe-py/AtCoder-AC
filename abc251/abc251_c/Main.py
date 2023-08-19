N = int(input())

visit = set()
point = 0
ans = 0

for i in range(N):
    s, t = map(str, input().split())
    if s not in visit:
        visit.add(s)
        if point < int(t):
            ans = i
            point = int(t)
print(ans + 1)