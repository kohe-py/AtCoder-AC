N = int(input())
K = int(input())

## 赤　青　黄

for _ in range(K):
    a, b = map(int, input().split())
    tmp = min(a, b, N - a + 1, N - b + 1)
    ans = tmp % 3
    if ans == 0:
        print(3)
    else:
        print(ans)
