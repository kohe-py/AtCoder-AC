T = int(input())

for i in range(T):
    count=0
    N = int(input())
    t = list(map(int, input().split()))
    for j in range(N):
        if t[j] % 2 == 1:
            count += 1
    print(count)