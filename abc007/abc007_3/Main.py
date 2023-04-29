from collections import deque

#入力
H, W = map(int, input().split())
sh, sw = map(int, input().split())
gh, gw = map(int, input().split())
sh -= 1
sw -= 1
gh -= 1
gw -= 1
maze = [[0] * W for _ in range(H)]
for i in range(H):
    maze[i] = input()


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
            
min_path = [[-1] * W for _ in range(H)]
todo = deque()
todo.append([sh,sw])
min_path[sh][sw] = 0

while len(todo) != 0:
    hw = todo.popleft()
    for d in range(4):
        nh = hw[0] + dx[d]
        nw = hw[1] + dy[d]
        
        if nh >= H or nw >= W or nw < 0 or nh < 0:
            continue
        if maze[nh][nw] == "#":
            continue
        if min_path[nh][nw] == -1:
            min_path[nh][nw] = min_path[hw[0]][hw[1]] + 1
            todo.append([nh, nw])

print(min_path[gh][gw])