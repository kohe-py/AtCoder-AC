N, M = map(int, input().split())

ans = [[-1] * N for _ in range(N)]
ans[0][0] = 0
d = []

for i in range(N):
    for j in range(N):
        if i ** 2 + j ** 2 == M:
            d.append([i, j])
            d.append([-i, j])
            d.append([-i, -j])
            d.append([i, -j])

        


from collections import deque
todo = deque()
todo.append([0, 0])
while todo:
    v = todo.popleft()
    for i, j in d:
        if 0 <= v[0] + i <= N - 1 and 0 <= v[1] + j <= N - 1 and ans[v[0] + i][v[1] + j] == -1:
            ans[v[0] + i][v[1] + j] = ans[v[0]][v[1]] + 1
            todo.append([v[0] + i, v[1] + j])

for i in range(N):
    print(*ans[i])
