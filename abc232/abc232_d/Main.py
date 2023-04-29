from collections import deque

H, W = map(int, input().split())
maze = [input() for _ in range(H)]


dx = [1, 0]
dy = [0, 1]
            
min_path = [[-1] * W for _ in range(H)]
todo = deque()
todo.append([0,0])
min_path[0][0] = 0
while len(todo) != 0:
    hw = todo.popleft()
    for d in range(2):
        nh = hw[0] + dx[d]
        nw = hw[1] + dy[d]
        
        if nh >= H or nw >= W or nw < 0 or nh < 0:
            continue
        if maze[nh][nw] == "#":
            continue
        if min_path[nh][nw] == -1:
            min_path[nh][nw] = min_path[hw[0]][hw[1]] + 1
            todo.append([nh, nw])
        
ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, min_path[i][j] + 1)
print(ans)