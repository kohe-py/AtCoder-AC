N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]


count = 0
while True:
    a = [[0] * N for _ in range(N)]
    count += 1
    flag = True
    for i in range(N):
        for j in range(N):
            a[i][j] = A[N-j-1][i]
            if a[i][j] == 1 and B[i][j] == 0:
                flag = False
    A = a
    #print("A", A)
    #print("B", B)
    if flag:
        print("Yes")
        exit()
    if count == 4:
        print("No")
        exit()