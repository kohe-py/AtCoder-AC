T = int(input())
for i in range(T):
    N = int(input())
    for j in range(2, N):
        if N % j == 0:
            X = j
            break
    if N % (j*j) == 0:
        print(j, N//(j*j))
    else:
        print(int((N//j)**(1/2)), j)