N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
for i in range(N):
    result += abs(A[i] - B[i])

if result > K:
    print("No")
elif result == K:
    print("Yes")
elif K % 2 == result % 2:
    print("Yes")
else:
    print("No")