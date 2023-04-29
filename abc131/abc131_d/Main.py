N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]

ab = sorted(ab, key = lambda x: x[1])
x = 0
for i in range(N):
    x += ab[i][0]
    if x <= ab[i][1]:
        pass
    else:
        print("No")
        exit()
print("Yes")