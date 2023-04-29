A = list(map(int, input().split()))
A.sort()
flag = 5
for i in range(len(A)-1):
    if A[i] != A[i+1]:
          flag = i
          break
if len(set(A)) == 2 and flag in {1, 2}:
  	print("Yes")
else:
  	print("No")