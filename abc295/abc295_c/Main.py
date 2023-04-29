from collections import Counter
N = int(input())
A = list(map(int, input().split()))

B = set(A)
ans = 0
c = Counter(A)
for i in B:
    x = c[i]
    ans += (x//2)
print(ans)