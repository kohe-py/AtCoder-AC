N = int(input())
C = []
A = []
for _ in range(N):
    c = int(input())
    a = set(map(int, input().split()))
    C.append(c)
    A.append(a)
X = int(input())

ans = []
for i in range(N):
    if X in A[i]:
        ans.append([i + 1, C[i]])
ans.sort(key = lambda x: x[1])
if len(ans) == 0:
    print(0)
    print(*[])
    exit()

result = []
flag = ans[0][1]

for i in range(len(ans)):
    if flag < ans[i][1]:
        break
    result.append(ans[i][0])

print(len(result))
print(*result)