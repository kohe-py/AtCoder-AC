N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))
B = [0] * (N+1)
for i in range(1, N+1):
    B[i] = B[i-1]+A[i-1]
#print(B)
b = set(B)
for i in range(len(B)):
    x = B[i]
    if x + P in b and x + P + Q in b and x+P+Q+R in b:
        print("Yes")
        exit()
        
print("No")