N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]

def cheack(result):
    flag = True
    flag1 = True
    flag2 = True
    for i in range(3):
        for j in range(3):
            if result[i][j] == ".":
                flag = False
            if result[-1-i][-j-1] == ".":
                flag1 = False
            if i == 2 and j == 2:
                if result[i + 1][j + 1] == "#":
                    flag2 = False
            elif i == 2:
                if result[i + 1][j] == "#":
                    flag2 = False
            elif j == 2:
                if result[i][j + 1] == "#":
                    flag2 = False
    
    if flag and flag1 and flag2:
        return True
    else:
        return False

ans = []
for i in range(N):
    for j in range(M):
        result = []
        if i + 8 <= N - 1 and j + 8 <= M - 1:
            for k in range(9):
                tmp = ""
                for l in range(9):
                    tmp += S[i + k][j + l]
                result.append(tmp)      
            if cheack(result):
                ans.append([i + 1, j + 1])

for i in range(len(ans)):
    print(*ans[i])
