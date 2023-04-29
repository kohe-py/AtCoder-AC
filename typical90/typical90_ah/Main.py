N, K = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict
d = defaultdict(int)
right = 0
kind = 0
ans = 1

for left in range(N):
    while right < N and kind <= K:
        if a[right] in d:
            d[a[right]] += 1
        else:
            d[a[right]] = 1
            kind += 1
        right += 1

    if kind <= K:
        ans = max(ans, right - left)
        break
    else:
        ans = max(ans, right - left - 1)
    d[a[left]] -= 1
    if d[a[left]] == 0:
        kind-= 1
        del d[a[left]]
print(ans)