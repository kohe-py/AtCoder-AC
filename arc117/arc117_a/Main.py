A, B = map(int, input().split())

ans = [0] * (A+B)
ans[0] = 1
if A > B:
    for i in range(A):
        ans[i] = ans[i-1] + 1
    for j in range(A, A+B-1):
        ans[j] = -ans[j-A]
    ans[A+B-1] = -sum(ans)

else:
    ans[0] = -1
    for i in range(B):
        ans[i] = ans[i-1] - 1 
    for j in range(B, A+B-1):
        ans[j] = -ans[j-B]
    ans[A+B-1] = -sum(ans)
    
print(*ans)