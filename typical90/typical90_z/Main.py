N = int(input())
g = [[] for _ in range(N+1)]

for _ in range(N - 1):
    A, B = map(int, input().split())
    g[A].append(B)
    g[B].append(A)


from collections import deque
color = [0] * (N + 1)
todo = deque()
todo.append(1)
color[1] = 1

while todo:
    v = todo.popleft()
    #print(v, color[v])
    c = color[v]
    for i in g[v]:
        if color[i] == 0:
            color[i] = -c
            todo.append(i)

answ = []
ansb = []
count = 0
cnt = 0
for i in range(1, N + 1):
    if color[i] == -1 and count <= N // 2 - 1:
        answ.append(i)
        count += 1
    if color[i] == 1 and cnt <= N // 2 - 1:
        ansb.append(i)
        cnt += 1

if count == N // 2:
    print(*answ)
else:
    print(*ansb)