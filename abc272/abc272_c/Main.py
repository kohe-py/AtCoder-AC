N = int(input())
A = list(map(int, input().split()))

A = sorted(A, reverse = True)
kisuu = []
guusuu = []
for i in range(len(A)):
    if A[i] % 2 == 0:
        guusuu.append(A[i])
    if A[i] % 2 == 1:
        kisuu.append(A[i])
        
s=-1
s1=-1
if len(kisuu) >= 2:
    s = kisuu[0] + kisuu[1]
if len(guusuu) >= 2:
    s1 = guusuu[0] + guusuu[1]
    
print(max(s, s1))