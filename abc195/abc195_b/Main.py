import bisect
A, B, W = map(int, input().split())

ans = []
W *= 1000
# goukei max, goukei min
Max = W // A
Min = W // B

for i in range(Min, Max+1):
    if A <= W / i <= B:
        ans.append(i) 

if len(ans) >= 1:
    print(ans[0], ans[-1])
else:
    print("UNSATISFIABLE")