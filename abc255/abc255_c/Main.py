X, A, D, N = map(int, input().split())

x = A + (N-1)*D
max_A = max(A, x)
min_A = min(A, x)

if D == 0:
    print(abs(A-X))
    exit()
if X < min_A:
    print(abs(min_A - X))
elif X > max_A:
    print(abs(X-max_A))
elif min_A <= X <= max_A:
    Y = X
    countp = 0
    countd = 0
    while True:
        if (X - A) % D == 0 or (Y - A) % D == 0:
            print(min(countp, countd))
            break
        X -= 1
        countp += 1
        Y += 1
        countd += 1