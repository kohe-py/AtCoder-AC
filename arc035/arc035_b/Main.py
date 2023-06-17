N = int(input())

t = [int(input()) for _ in range(N)]
import math

t.sort()
now = 0
ans = 0
for i in range(N):
    ans += (now + t[i])
    now += t[i]

print(ans)
same = [1]
for i in range(N - 1):
    if t[i] == t[i + 1]:
        same[-1] += 1
    else:
        same.append(1)
    
#print(same)
count = 1
for i in range(len(same)):
    count *= math.factorial(same[i])
    count %= (10 ** 9 + 7)
print(count)