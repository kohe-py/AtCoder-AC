H,W = map(int, input().split())
C = [input() for _ in range(H)]
#print(C)
X = []
for i in range(W):
    c = 0
    for j in range(H):
        if C[j][i] == "#":
            c += 1
    X.append(c)
print(*X)