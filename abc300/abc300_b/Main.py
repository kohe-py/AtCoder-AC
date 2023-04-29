from collections import deque
H, W = map(int ,input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]

a = deque()
countB = 0
countA = 0
for i in range(H):
    a.append(deque(A[i]))
    for j in range(W):
        if A[i][j] == "#":
            countA += 1
        if B[i][j] == "#":
            countB += 1

if countA != countB:
    print("No")
    exit()

            
for i in range(H + 1):
    if i == 0:
        pass
    else:
        x = a.pop()
        a.appendleft(x)
    for j in range(W + 1):
        flag = True
        count = 0
        if j == 0:
            pass
        else:
            for v in range(H):
                x = a[v].pop()
                a[v].appendleft(x)
            #print(*a, sep="\n")
            #print("-----------")
            #print(*B, sep="\n")
        for ii in range(H):
            for jj in range(W):
                if a[ii][jj] == B[ii][jj]:
                    count += 1
                else:
                    break
        if count == H * W:
            print("Yes")
            exit()


exit(print("No"))
