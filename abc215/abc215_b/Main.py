N = int(input())
k = 0
while True:
  result = 2 ** k 
  if result > N:
    break
  k+=1
  
print(k-1)