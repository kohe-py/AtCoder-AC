N,M = map(int, input().split())
a = list(map(int, input().split()))
b = list(range(1, N+1))

if M == 0:
    print(*b)
    exit()
    
count = 1
ans = []
a.append(-1)
for i in range(M):
    if a[i]+1 == a[i+1]:
            k = a[i+1]
            x = a[i+1]
            count+= 1
    elif count == 1:
        b[a[i]], b[a[i]-1] = b[a[i]-1], b[a[i]]
        
    else:
        b[x-count:x+1] = reversed(b[x-count:x+1])
        #print(*b)
        count = 1
        
print(*b)