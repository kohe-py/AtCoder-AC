N = int(input())
P = list(map(int, input().split()))

count = 1
e = [P[-1]]
for i in reversed(range(N)):
    if i - 1 >= 0:
        if P[i] > P[i - 1]:
            e.append(P[i - 1])
            count += 1
        else:
            #e.append(P[i - 1])
            head = P[i - 1]
            #count += 1
            break

import bisect
e.sort()
head_new = bisect.bisect_right(e, head)
ans = P[:N - count - 1] + [e[head_new - 1]]
e[head_new - 1] = head
for i in reversed(range(count)):
    ans.append(e[i])
print(*ans)
