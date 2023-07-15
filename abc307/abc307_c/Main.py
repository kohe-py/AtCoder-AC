H, W = map(int, input().split())
A = [input() for _ in range(H)]
H1, W1 = map(int, input().split())
B = [input() for _ in range(H1)]
y,x = map(int, input().split())
X = [list(input()) for _ in range(y)]

import copy

#トリミング
def tori(H, W, A):
    count = 0
    h = -1
    h_m = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] == "#":
                if count == 0:
                    h = i - 1
                    count += 1
                h_m = i + 1
    count = 0
    w = -1
    w_m = 0
    for j in range(W):
        for i in range(H):
            if A[i][j] == "#":
                if count == 0:
                    w = j - 1
                    count += 1
                w_m = j + 1
    
    ans = [["."] * (w_m - w - 1) for _ in range(h_m - h - 1)]
    for i in range(h_m - h - 1):
        for j in range(w_m - w - 1):
            ans[i][j] = A[h + 1 + i][w + 1 + j]
    
    return ans

A = tori(H, W, A)
B = tori(H1, W1, B)

leng_H = len(X)
leng_W = len(X[0])
H = len(A)
W = len(A[0])
h = len(B)
w = len(B[0])

def cheack(H, W, ans, X):
    for i in range(H):
        for j in range(W):
            if ans[i][j] != X[i][j]:
                return False
    return True
flag = False
for i in range(leng_H):
    if i + H - 1 > leng_H - 1:
        continue
    for j in range(leng_W):
        if j + W - 1 > leng_W - 1:
            continue
        ans = [["."] * leng_W for _ in range(leng_H)]
        for x in range(H):
            for y in range(W):
                ans[i + x][j + y] = A[x][y]

        for k in range(leng_H):
            if k + h - 1 > leng_H - 1:
                      continue
            for l in range(leng_W):
                if l + w - 1 > leng_W - 1:
                    continue
                ans1 = copy.deepcopy(ans)
                for x in range(h):
                    for y in range(w):
                        if ans1[k + x][l + y] == "#":
                            continue
                        ans1[k + x][l + y] = B[x][y]

                if cheack(leng_H, leng_W, ans1, X):
                    flag = True
        
if flag:
    print("Yes")
else:
    print("No")