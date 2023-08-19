N = int(input())
A = list(map(int, input().split()))
result = 0
def dfs(s, A, result):
    ans, todo, visit = [s+1], [s], {s}
    while todo:
        v = todo.pop()
        if A[v] - 1 in visit:
            result =  A[v]
            return ans, result
        else:
            todo.append(A[v] - 1)
            ans.append(A[v])
            visit.add(A[v] - 1)

ans, flag = [], False
x, result = dfs(0, A, result)
for i in x:
    if i == result:
        flag = True
    if flag:
        ans.append(i)
print(len(ans))
print(*ans)