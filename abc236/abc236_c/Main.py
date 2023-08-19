N, M = map(int, input().split())
S = input().split()
T = input().split()

t = set(T)
for i in range(N):
    if S[i] in t:
        print("Yes")
    else:
        print("No")