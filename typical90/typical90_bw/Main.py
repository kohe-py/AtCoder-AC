N = int(input())

import math
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


x = factorization(N)
if len(x) == 1 and x[0][1] == 1:
    print(0)
    exit()

count = 0
for i in range(len(x)):
    count += x[i][1]

ans = 0
i = 1
while True:
    count /= 2
    count = math.ceil(count)
    if count <= 1:
        break
    i += 1

print(i) 

