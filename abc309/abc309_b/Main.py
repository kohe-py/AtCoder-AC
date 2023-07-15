N = int(input())
A = [list(input()) for _ in range(N)]

B = [[""] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == 0 or j == 0 or i == N - 1 or j == N - 1:
            if i == 0 and j == N - 1:
                B[i + 1][j] = A[i][j]
            elif i == 0 and j <= N - 2:
                B[i][j + 1] = A[i][j]
            elif j == N - 1:
                if i == N - 1:
                    B[i][j - 1] = A[i][j]
                else:
                    B[i + 1][j] = A[i][j]
            elif i == N - 1:
                if j == 0:
                    B[i - 1][j] = A[i][j]
                else:
                    B[i][j - 1] = A[i][j]
            elif j == 0:
                B[i - 1][j] = A[i][j]

        else:
            B[i][j] = A[i][j]

for i in range(N):
    print("".join(B[i]))

