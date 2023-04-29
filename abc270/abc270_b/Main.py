X,Y,Z=map(int, input().split())

ans = 0
if Y < 0:
    X *= -1
    Y *= -1
    Z *= -1
    
if X < Y:
    ans = abs(X)
    
elif X > Y:
    ans += abs(Z)
    ans += abs(Z-X)
    if Y < Z < X or Y < X < Z:
        print(-1)
        exit()
    

print(ans)