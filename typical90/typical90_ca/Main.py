H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

ans = 0
for i in range(H):
    for j in range(W):
        count = B[i][j] - A[i][j]
        ans += abs(count)
        if i < H - 1 and j < W - 1:
            A[i][j] += count
            A[i][j+1] += count
            A[i+1][j] += count
            A[i+1][j+1] += count
        if i == H - 1:
            if A[i][j] == B[i][j]:
                pass
            else:
                print("No")
                exit()
        if j == W - 1:
            if A[i][j] == B[i][j]:
                pass
            else:
                print("No")
                exit()
print("Yes")
print(ans)