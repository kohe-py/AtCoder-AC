N = int(input())
H = list(map(int, input().split()))

m = 0
x = 0
for i in range(N):
    if H[i] >= x:
        m = i+1
        x = H[i]
print(m)