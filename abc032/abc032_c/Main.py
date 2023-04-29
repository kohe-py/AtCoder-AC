N, K = map(int, input().split())
s = [int(input()) for _ in range(N)]

from collections import defaultdict
d = defaultdict(int)
seki = 1
right = 0
ans = 1
count = 0

for left in range(N):
    if s[left] > K:
        count += 1

    if s[left] == 0:
        exit(print(N))

    if left != 0:
        seki //= s[left - 1]

    while seki <= K and right < N:
        seki *= s[right]
        if seki > K and s[right] != 0:
            seki //= s[right]
            break
        right += 1
    ans = max(ans, right - left)

if count == N:
    print(0)
    exit()
else:
    print(ans)