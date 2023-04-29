N, X = map(int, input().split())
S = input()

X = list(bin(X))
for i in range(N):
    if S[i] == "U":
        X.pop()
    elif S[i] == "L":
        X.append("0")
    else:
        X.append("1")
print(int("".join(X), 2))