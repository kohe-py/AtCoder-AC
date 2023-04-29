N=int(input())
P=[0,0]+list(map(int,input().split()))
crr=N  
cnt=0  
while crr!=1:
  cnt+=1
  crr=P[crr]
print(cnt)