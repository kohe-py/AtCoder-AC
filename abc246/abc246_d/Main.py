N = int(input())

def birary(n, i):
    left = 0
    right = 10**6
    
    while (right - left) >= 0:
        center = left + (right - left)//2
        if (i ** 3) + (i ** 2) * center + i * (center ** 2) + (center ** 3) < N:
            left = center + 1
        elif (i ** 3) + (i ** 2) * center + i * (center ** 2) + (center ** 3) > N:
            right = center - 1
        else:
            return center
    return left
 
ans = 10 ** 18
for i in range(10 ** 6 + 1):
    result = birary(N, i)
    f = (i ** 3) + (i ** 2) * result + (i * (result ** 2)) + (result ** 3)
    if N <= f < ans:
        ans = f
    #print(ans)
print(ans)