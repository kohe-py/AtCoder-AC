from collections import deque
N = int(input())
p = deque(map(int, input().split()))

count = [0] * N
for i in range(N):
    a = (p[i]-i -1)%N
    b = (p[i]-i)%N
    c = (p[i] - i +1)%N
    count[a] += 1
    count[b] += 1
    count[c] += 1
print(max(count))