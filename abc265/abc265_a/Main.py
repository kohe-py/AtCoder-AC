X, Y, N = map(int, input().split())
if X*3 <= Y:
    print(X*N)
else:
    y = (N//3) * Y
    x = (N - N//3 * 3) * X
    print(y+x)