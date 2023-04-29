N,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
def yuka(A,k):
    c=0
    for i in range(N):
        c += k//A[i]
    return c

right=10 ** 9
left=1
k = 0
while right-left>0:
    center=(right+left)//2
    #print(center)
    if yuka(A,center)>=K:
        right=center
    elif yuka(A,center)<K:
        left=center+1

print(left)