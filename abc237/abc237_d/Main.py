from collections import deque
N = int(input())
S = input()

A = deque()
A.append(N)
for i in range(N):
    if S[N-1-i] == "L":
        A.append(N-1-i)
    else:
        A.appendleft(N-1-i)
print(*A)