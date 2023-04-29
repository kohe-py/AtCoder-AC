H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

for bit in range(1<<H):
    count = 0
    new_h = []
    for i in range(H):
        if bit & (1 << i):
            count += 1
            new_h.append(i)
    if count != H2:
        continue
    else:
        for bit in range(1 << W):
            count = 0
            new_w = []
            for j in range(W):
                if bit & (1 << j):
                    count += 1
                    new_w.append(j)
            if count != W2:
                continue
            else:
                c = 0
                for i in range(H2):
                    for j in range(W2):
                        if A[new_h[i]][new_w[j]] == B[i][j]:
                            c += 1
                if c == W2 * H2:
                    print("Yes")
                    exit()
                    
print("No")