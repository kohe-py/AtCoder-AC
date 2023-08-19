N = int(input())
A = list(map(int, input().split()))

A.sort()
ans = 0
ave = sum(A) // N
up, down = 0, 0
for i in range(N):
    if A[i] > ave:
        down += abs(ave - A[i] + 1)
    elif A[i] < ave:
        up +=  abs(ave - A[i])
#print(up, down)
print(max(up, down))
