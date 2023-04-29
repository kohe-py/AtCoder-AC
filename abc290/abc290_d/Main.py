import math
for _ in range(int(input())):
    N, D, K = map(int, input().split())
    g = math.gcd(N, D)
    K -= 1
    A = N // g
    print((D * K + K // A) % N)
