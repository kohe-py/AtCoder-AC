N, K, A = map(int, input().split())


while True:
    K -= 1
    if K == 0:
        break
    A += 1
    if A == N + 1:
        A = 1
print(A)