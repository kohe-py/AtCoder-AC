H, W, N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(M)]

# ブロック-1　光なし０　光あり２
ans = [[0] * W for _ in range(H)]
ans2 = [[0] * W for _ in range(H)]

# ブロックの位置
for i, j in CD:
    ans[i - 1][j - 1] = -1
    ans2[i - 1][j - 1] = -1
#print(ans)

def search(x, y, grid):
    i, j = x, y
    while i < H and grid[i][j] == 0:
        ans[i][j] = 2
        i += 1
        #print("1", ans)
    i, j = x - 1, y
    while 0 <= i and grid[i][j] == 0:
        grid[i][j] = 2
        i -= 1
        #print("1", ans)

def search2(x, y, grid):
    i, j = x, y
    while j < W and grid[i][j] == 0:
        grid[i][j] = 2
        j += 1
        #print("2", ans)
    i, j = x, y - 1
    while 0 <= j and grid[i][j] == 0:
        grid[i][j] = 2
        j -= 1
        #print("2", ans)

#　電球を考える
for x, y in AB:
    search(x-1, y-1, ans)
    search2(x-1, y-1, ans2)

count = 0
for i in range(H):
    for j in range(W):
        if ans[i][j] + ans2[i][j] >= 1:
            count += 1
print(count)

