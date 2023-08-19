M = int(input())
D = list(map(int, input().split()))

Sum = sum(D)
center = Sum // 2 + 1
i = 0
tmp = 0
while True:
    if i == M:
        break
    if tmp + D[i] >= center:
        break
    tmp += D[i]
    i += 1

month = i + 1
day = center - tmp
print(month, day)