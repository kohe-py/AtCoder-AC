from collections import deque
N = int(input())
a = list(map(int, input().split()))

b = [False] * N
count_true = 0
for i in range(N):
    if i+1 == a[i]:
        b[i] = True
        count_true += 1
        
b = deque(b) 
count = 0
for i in range(N):
    v = b.popleft()
    if v:
        count_true -= 1
    if a[i] == i+1:
        count += count_true
        
    else:
        k = a[i]
        if i <= k-1 and a[k-1] == i+1:
            count += 1
            
print(count)