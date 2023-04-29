N, A, B, C, D = map(int, input().split())

if N <= 2:
    print("Yes")
    exit()
if A == N - 1 or D == N - 1:
    print("Yes")
    exit()
if B == N - 1 or C == N - 1:
    print("No")
    exit()
if A + D == N - 1:
    print("No")
    exit()

if abs(B - C) >= 2:
    print("No")
    exit()
    
print("Yes")