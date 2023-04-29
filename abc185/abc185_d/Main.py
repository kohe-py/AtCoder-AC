N, M = map(int, input().split())
A = list(map(int, input().split()))
if M == 0:
  print(1)
  exit()
if M == N:
  print(0)
  exit()
def GCD(A, B):
    if B == 0:
        return A
    r = A % B
    return GCD(B, r)
A.sort()
a = []
if A[0] != 1:
    a.append(A[0]-1)
for i in range(1,M):
    if abs(A[i] - A[i-1])-1 != 0:
        a.append(abs(A[i] - A[i-1])-1)
if N - A[-1] != 0:
    a.append(abs(N-A[-1]))

x = min(a)
count = 0
for i in range(len(a)):
    if a[i] % x == 0:
        count += (a[i]//x)
    else:
        count += (a[i]//x)
        count +=1
    #print(a[i], x, count)

print(count)