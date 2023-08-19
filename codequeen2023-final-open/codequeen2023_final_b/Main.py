N = int(input())
g = [["."] * N for _ in range(N)]
from collections import defaultdict

h = defaultdict(int)
w = defaultdict(int)
hw = defaultdict(int)
hw2 = defaultdict(int)

for _ in range(N - 1):
    r, c = map(int, input().split())
    g[r - 1][c - 1] = "#"
    h[r - 1] += 1
    w[c - 1] += 1
    if r >= c:
        hw[(r - c, 0)] += 1
    else:
        hw[(0, c - r)] += 1
    if N >= r + c:
        hw2[(0, r + c - 2)] += 1
    else:
        hw2[(r + c - 2, N - 1)] += 1

for i in range(N):
    for j in range(N):
        if g[i][j] == ".":
            if h[i] == 0 and w[j] == 0:
                if i >= j:
                    if hw[(i - j, 0)] == 0 and hw2[(i + j, N - 1)] == 0:
                        if N - 1 >= i + j + 1 and hw2[(0, i + j)] == 0:
                            print(i + 1, j + 1)
                            exit()
                        elif N - 1 < i + j + 1 and hw2[(0, i + j)] == 0:
                            print(i + 1, j + 1)
                            exit()
                else:
                    if hw[(0, j - i)] == 0 and hw2[(0, i + j)] == 0:
                        if N - 1 >= i + j + 1 and hw2[(0, i + j)] == 0:
                            print(i + 1, j + 1)
                            exit()
                        elif N - 1 < i + j + 1 and hw2[(0, i + j)] == 0:
                            print(i + 1, j + 1)
                            exit()
            
print(-1)