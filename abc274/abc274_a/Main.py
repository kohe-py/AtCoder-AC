A,B=map(int, input().split())

x = B // A
y = round(1000 * (B / A - x))
print("{}.{:03d}".format(x, y))