Q = int(input())
x = [int(input()) for _ in range(Q)]

for i in range(Q):
    j = 2
    while True:
        if j > x[i] ** (1/2):
            print("Yes")
            break
        if x[i] % j == 0:
            print("No")
            break
        if j >= 3:
            j += 2
        else:
              j += 1