L, X, Y, S, D = map(int, input().split())

ans1 = 0
ans2 = 10 ** 18

if D <= S:
    ans1 = ((L - S) + D) / (X + Y)
else:
    ans1 = (D - S) / (X + Y)

if Y > X:
    if D <= S:
        ans2 = (S - D) / (Y - X)
    else:
        ans2 = (S + (L - D)) / (Y - X)
print(min(ans1, ans2))