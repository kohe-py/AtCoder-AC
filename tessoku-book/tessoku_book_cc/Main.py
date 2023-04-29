N = input()

ans = 0
for i in range(len(N)):
    ans += 2 ** (len(N) -  i - 1) * int(N[i])

print(ans)