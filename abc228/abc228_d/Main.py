Q = int(input())

N = 2 ** 20
A = [-1] * (N)
index = list(range(N))

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        h = x
        while A[h % N] != -1:
            h = (index[h % N] + 1)
        A[h % N] = x
        index[x % N] = (h % N)

    if t == 2:
        #rint(A[0])
        print(A[(x % N)])