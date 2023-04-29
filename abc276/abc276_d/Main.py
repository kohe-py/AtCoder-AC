N = int(input())
A = list(map(int, input().split()))

if len(set(A)) == 1:
    print(0)
    exit()
max2 = 0
min2 = 10**9
max3 = 0
min3 = 10**9
B_2 = [0 for _ in range(N)]
B_3 = [0 for _ in range(N)]
B = [1 for _ in range(N)]
for i in range(N):
    if A[i] % 2 == 0:
        while A[i] % 2 == 0:
            A[i] //= 2
            B_2[i] += 1
    max2 = max(max2, B_2[i])
    min2 = min(min2, B_2[i])
    if A[i] % 3 == 0:
        while A[i] % 3 == 0:
            A[i] //= 3
            B_3[i] += 1
    max3 = max(max3, B_3[i])            
    min3 = min(min3, B_3[i])
    B[i] = A[i]

if len(set(B)) != 1:
    print(-1)
    exit()

ans = 0
for i in range(N):
    if B_2[i] != min2:
        ans += (B_2[i] - min2)
    if B_3[i] != min3:
        ans += (B_3[i] - min3)
print(ans)