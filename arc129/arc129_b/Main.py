N = int(input())

right = 10 ** 18
left = 0
for _ in range(N):
    L, R = map(int, input().split())
    left = max(left, L)
    right = min(right, R)
    x = (right + left) // 2
    x = abs(x)
    r = x - right
    l = left - x

    print(max(0, r, l))
    
