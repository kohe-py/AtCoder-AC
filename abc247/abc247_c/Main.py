N = int(input())
def main(n):
    if n == 1:
        return [1]
    else:
        return main(n - 1) + [n] + main(n - 1)
y = main(N)
print(*y)