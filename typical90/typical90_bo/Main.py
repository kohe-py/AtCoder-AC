N, K = map(int, input().split())

def base10toN(number, n):
    result = ""
    while True:
        x = number % n
        result = str(x) + result
        number //= n
        if number == 0:
            break
    return result

for i in range(K):
    N = int(str(N), 8)
    N = base10toN(N, 9)
    N = N.replace("8", "5")
print(N)
