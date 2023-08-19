from collections import deque

N, M = map(int, input().split())
g = [set() for _ in range(N)]

ans = set()
for _ in range(M):
    flag = True
    A, B = map(int, input().split())
    g[A - 1].add(B - 1)
    ans.discard(B - 1)
    todo = deque(ans)
    visit = ans.copy()
    while todo:
        v = todo.popleft()
        for i in g[v]:
            if A - 1 == i:
                flag = False
            if i not in visit:
                visit.add(i)
                todo.append(i)
    if flag:
        ans.add(A - 1)


if len(ans) == 1:
    for i in ans:
        print(i + 1)
else:
    print(-1)
