N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

week = B[0][0] % 7
if week == 0:
    if M >= 2:
        print("No")
        exit()
else:
    if week + M - 1 > 7:
        print("No")
        exit()

for i in range(N):
    for j in range(M):
        if i > 0 and B[i][j] != B[i - 1][j] + 7 and B[i - 1][j] >= j + 1 and B[i][j] <= B[i][0] + M - 1:
            print("No")
            exit()
        if j > 0 and B[i][j] != B[i][j - 1] + 1 and B[i][j - 1] >= j:
            print("No")
            exit()

print(("Yes"))