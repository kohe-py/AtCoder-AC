H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

flag = 0
a, b, c, d = (-1, -1), (-1, -1), (-1, -1), (-1, -1)
for i in range(H):
    for j in range(W):
        if 0 < j < W - 1 and S[i][j] == "." and S[i][j - 1] == "#" and S[i][j + 1] == "#":
            print(i + 1, j + 1)
            exit()
        # 左上
        if i < H - 1 and j + 1 <= W - 1:
            if S[i][j] == "." and S[i][j + 1] == "#" and S[i + 1][j] == "#":
                print(i + 1, j + 1)
                exit()
        # 右上
        if i < H - 1 and 0 < j:
            if S[i][j] == "." and S[i][j - 1] == "#" and S[i + 1][j] == "#":
                print(i + 1, j + 1)
                exit()
        if j + 1 <= W - 1 and 0 < i:
            if S[i][j] == "." and S[i][j + 1] == "#" and S[i - 1][j] == "#":
                print(i + 1, j + 1)
                exit()
        if 0 < i and 0 < j:
            if S[i][j] == "." and S[i][j - 1] == "#" and S[i - 1][j] == "#":
                print(i + 1, j + 1)
                exit() 
        
        