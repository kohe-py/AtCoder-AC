H, W = map(int, input().split())
C = [input() for _ in range(H)]

N = min(H, W)
ans = [0 for _ in range(N)]

for i in range(1, H - 1):
    for j in range(1, W - 1):
        if C[i][j] == "#":
            x, y = 1, 1
            count = 0
            while True:
                if i + y <= H - 1 and j + x <= W - 1 and 0 <= i - y and 0 <= j - x and (C[i + y][j + x] == "#" and C[i - y][j + x] == "#" and C[i + y][j - x] == "#" and C[i - y][j - x] == "#"):
                    count += 1
                    x += 1
                    y += 1
                    #print(count)
                    #print("afjsdkl;")
                else:
                    if count != 0:
                        ans[count - 1] += 1
                    break

print(*ans)