N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

print(min(min(D) + Q, P))