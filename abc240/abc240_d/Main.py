from collections import deque
N = int(input())
a = list(map(int, input().split()))

result = []
length = 0
for i in range(N):
    if len(result) == 0:
        result.append([a[i], 1])
        length += 1
        
    elif result[-1][0] == a[i]:
        result[-1][1] += 1
        length += 1
        if result[-1][1] == a[i]:
            length -= a[i]
            result.pop()
    else:
        result.append([a[i], 1])
        length += 1
    print(length)