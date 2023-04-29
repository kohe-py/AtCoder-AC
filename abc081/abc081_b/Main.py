N = int(input())
A = list(map(int, input().split()))
count = 0
flag = 0

while True:
    for i in range(N):
        if A[i] % 2 != 0:
            flag = 1
    if flag == 1:
        break
    for i in range(N):
        A[i] /= 2
    count += 1
        
print(count)