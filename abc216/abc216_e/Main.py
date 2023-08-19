N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = 0
count = 0
A.append(0)

for i in range(N):
    c = (i + 1) * (A[i] - A[i + 1])
    if count + c > K:
        diff = (K - count)
        mod = diff % (i + 1)
        howmany = diff // (i + 1)
        ans += (i + 1) * (howmany) * (2 * A[i] - howmany + 1) // 2
        ans += mod * (A[i] - howmany)
        break
    ans += c * (A[i] + A[i + 1] + 1) // 2
    count += c
    A[i] = A[i + 1]
    if count == K:
        print(ans)
        exit()
    elif count < K and i == N - 1:
        print(ans)
        exit()

print(ans)
