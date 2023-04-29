N = int(input())
A = list(map(int, input().split()))

s = set()
ans = list(range(1, N+1))
ans = set(ans)
for i in range(1, N+1):
    if i not in s:
        if A[i-1] in ans:
            ans.remove(A[i-1])
            s.add(A[i-1])
ans = list(ans)
ans.sort()
print(len(ans))
print(*ans)