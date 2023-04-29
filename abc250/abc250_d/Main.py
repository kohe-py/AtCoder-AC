N = int(input())
flag = int(N ** (1/3))
nlist = [True] * (flag+1)
nlist[0] = False
nlist[1] = False

for i in range(2, flag+1):
    if nlist[i] == False:
        continue
    for j in range(i * 2, flag+1, i):
        nlist[j] = False
    
result = []
for i in range(flag+1):
    if nlist[i]:
        result.append(i)
#print(*result)
count = 0
for i in range(len(result)):
    y = result[i]
    for j in range(i+1,len(result)):
        x = y * (result[j]**3)
        if N < x:
            break
        count += 1
        
print(count)