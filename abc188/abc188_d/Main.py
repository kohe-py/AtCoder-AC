N, C = map(int, input().split())

abc = [list(map(int, input().split())) for _ in range(N)]

B = []
for i in range(N):
    a, b, c = abc[i]
    B.append((a, c))
    B.append((b + 1, -c))

B = sorted(B, key=lambda x: x[0])
ans = 0
now = 0
value = 0
for t, c in B:
    if t != now:
        ans += min(value, C) * (t - now)
        now = t
    value += c

print(ans)