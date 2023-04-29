N=int(input())
left=0
right=N
while right-left>0.00000001:
    center=(right+left)/2
    y=center**3+center
    #print(y)
    if y<N:
        left=center
    elif y>=N:
        right=center
    #print(left, right)
        
print(left)