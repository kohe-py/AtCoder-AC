N,X=map(int,input().split())
A=list(map(int,input().split()))

right=len(A)-1
left=0

while right-left>=0:
    center=left+(right-left)//2
    if A[center]>X:
        right=center-1
    elif A[center]<X:
        left=center+1
    else:
        break
    
print(center+1)