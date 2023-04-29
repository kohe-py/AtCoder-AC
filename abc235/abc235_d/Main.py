from collections import deque
a, N = map(int, input().split())

max_len = len(str(N))
todo = deque()
dist = [10**18] * (int("9" * max_len)+1)
s = set()

todo.append(1)
dist[1] = 0

while len(todo) != 0:
    #print(todo)
    x = todo.popleft()
    if x * a <= int("9" * max_len):
        if x*a not in s:
            todo.append(x*a)
            dist[x*a] = min(dist[x*a], dist[x] + 1)
            s.add(x*a)

    if x >= 10 and x % 10 != 0:
        x_str = str(x)
        y_str = x_str[-1] + x_str[:-1]
        y = int(y_str)
        if y not in s:
            todo.append(y)
            dist[y] = min(dist[y], dist[x] + 1)
            s.add(y)
        
        
    


#print(dist)
if dist[N] == 10**18:
    print(-1)
else:
    print(dist[N])