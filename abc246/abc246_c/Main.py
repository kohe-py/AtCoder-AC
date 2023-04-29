N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A, reverse = True)
ans = sum(A)
flag = False
for i in range(N):
    k = A[i] // X
    #print(k)
    if K < k:
        #print("afjsdkl;")
        k = K
        flag = True
    elif K > k:
        K -= k
    else:
        flag = True
    ans -= min(A[i], k * X)
    A[i] = max(0, A[i] - (k * X))
    if flag:
        print(ans)
        exit()

A = sorted(A, reverse = True)
i = 0
while True:
    ans -= A[i]
    K -= 1
    i += 1
    if K == 0 or i == N:
        break

print(ans)