from collections import defaultdict
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


count = 0
for bit in range(1 << H+W-1):
    #print(bin(bit))
    s = {A[0][0], A[H-1][W-1]}
    start = [1,1]
    countH = 0
    countW = 0
    for i in range(H+W):
        if bit & (1 << i):
            #print(start)
            start[0] += 1
            if start[0] >= H+1:
                break
            s.add(A[start[0]-1][start[1]-1])
            countH += 1
        else:
            start[1] += 1
            if start[1] >= W+1:
                break
            countW += 1
            s.add(A[start[0]-1][start[1]-1])
    #print(countH, countW, len(s))
    #print(countH, countW, s)
    if countH == H-1 and countW == W-1:
        if len(s) == H+W-1:
            count += 1
print(count//2)

