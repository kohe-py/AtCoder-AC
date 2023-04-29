N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dpa = [False] * (N+1)
dpb = [False] * (N+1)
dpa[0] = True
dpb[0] = True
for i in range(N-1):
    if dpa[i] == True:
        if abs(A[i] - A[i+1]) <= K:
            dpa[i+1] = True
        if abs(A[i] - B[i+1]) <= K:
            dpb[i+1] = True
    if dpb[i] == True:
        if abs(B[i] - A[i+1]) <= K:
            dpa[i+1] = True
        if abs(B[i] - B[i+1]) <= K:
            dpb[i+1] = True

            
if dpa[N-1] or dpb[N-1]:
    print("Yes")
else:
    print("No")