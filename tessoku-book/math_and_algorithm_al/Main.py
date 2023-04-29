T = int(input())
N = int(input())
B = [0] * (T+1)
for i in range(N):
    L, R = map(int, input().split())
    B[L] += 1
    B[R] -= 1
A=[B[0]]
for i in range(1, T+1):
    A.append(A[i-1] + B[i])
#print(A)
for i in range(len(A)-1):
    print(A[i])