N, K = map(int, input().split())
A = list(map(int, input().split()))

ind = [0] * N
for i in range(N):
    ind[A[i] - 1] = i

def re(l, r):
    if r < N - 1:
        return A[:l] + list(reversed(A[l:r + 1])) + A[r + 1:]
    elif r == N - 1:
        return A[:l] + list(reversed(A[l:r + 1]))
    
count = 0
flag = True
visit = set()
for i in range(N):
    for j in range(N):
        if j in visit:
            continue
        if ind[j] == i:
            count += (((N - 2 - i) * (N - i - 1)) // 2)
            count += N
        else:
            count += 1
            if count == K:
                print(*re(i, ind[j]))
                exit()

        if count > K:
            count -= (((N - i - 2) * (N - i - 1)) // 2)
            count -= N
            visit.add(j)
            break

print(*A)