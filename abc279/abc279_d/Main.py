from scipy import optimize


A, B = map(int, input().split())
g = 1
def f(x):
    return B * abs(int(x)) + A / (g + abs(int(x))) ** (1/2)


x_min = optimize.brent(f)
print(f(x_min))