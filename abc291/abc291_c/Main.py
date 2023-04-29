from collections import deque
N = int(input())
S = input()

visited = set()
visited.add((0, 0))
todo = deque()
todo.append([0, 0])
for i in range(N):
    v = todo.popleft()
    if S[i] == "R":
        x = v[0] + 1
        y = v[1]
        if (x, y) in visited:
            print("Yes")
            exit()
        visited.add((x, y))
    elif S[i] == "L":
        x = v[0] - 1
        y = v[1]
        if (x, y) in visited:
            print("Yes")
            exit()
        visited.add((x, y))
    elif S[i] == "U":
        x = v[0]
        y = v[1] + 1
        if (x, y) in visited:
            print("Yes")
            exit()
        visited.add((x, y))
        
    else:
        x = v[0]
        y = v[1] - 1
        if (x, y) in visited:
            print("Yes")
            exit()
        visited.add((x, y))
    todo.append((x, y))
        
print("No")  