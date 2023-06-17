N = int(input())
if N % 10 < 3:
    print(N // 10 * 10)
elif N % 10 == 5:
    print(N)
else:
    print(N // 10 * 10 + 5)