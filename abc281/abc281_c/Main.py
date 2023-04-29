N, T = map(int, input().split())
A = list(map(int, input().split()))

B = [A[0]]
for i in range(1, N):
    B.append(B[i-1] + A[i])
    
result = T % B[N-1]

i = 0
while result>0:
    result -= A[i]
    i += 1

print(i, A[i - 1] + result)