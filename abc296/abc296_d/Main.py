N, M = map(int, input().split())

#1以上N以下の整数a,bの積
#其の積はM以上

def bisect(x, n, a):
    left = 1
    right = N
    while left - right <= 0:
        center = left + (right - left) // 2
        if a * center == x:
            return center
        
        elif a * center < x:
            left = center + 1

        else:
            right = center - 1

    if center * a < x:
        return center + 1
    else:
        return center

if N**2 < M:
    print(-1)
    exit()

if N >= M:
    print(M)
    exit()
else:
    #2つのN以下の整数a,bでできるM以上で最小のX
    # a <= b 
    ans = 10**12
    a = 1
    while a <= int(M**(1/2)) + 1:
        #print(bisect(M,N,a))
        if a * N >= M:
            y = bisect(M, N, a)
            #print(y)
            ans = min(ans, y*a)
        a += 1

print(ans)