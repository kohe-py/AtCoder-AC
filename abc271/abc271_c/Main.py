from collections import deque
N = int(input())
a = list(map(int, input().split()))

a.sort()
b = set(a)
M = len(b)
A = deque(b)
for i in range(N-M):
    A.append(10**9)

ans = 0
request = 1
#print(a)
while A:
    x = A.popleft()
    if x == request:
        ans += 1
        request += 1

    else:
        A.appendleft(x)
        if len(A) >= 2:
            sell_1 = A.pop()
            sell_2 = A.pop() 
            A.appendleft(request)
            #print(a)
            continue
        else:
            break

print(ans)