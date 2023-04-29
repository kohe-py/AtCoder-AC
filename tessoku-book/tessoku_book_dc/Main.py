H, W = map(int, input().split())

def combo(N, R):
    a = 1
    b = 1
    M = 1000000007
    for i in range(1, N+1):
        a = (a * i) % M
    for i in range(1, R+1):
        b = (b * i) % M
    for i in range(1, N - R + 1):
        b = (b * i) % M 
    return (a * pow(b, M-2, M)) % M

print(combo(H+W-2, H-1))