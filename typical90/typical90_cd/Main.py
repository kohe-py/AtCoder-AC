L, R = map(int, input().split())

keta_min = len(str(L))
keta_max = len(str(R))
mod = 10**9 + 7
if keta_max == keta_min:
    print((R + L) *(R - L + 1) // 2 * keta_min % mod)
    exit()
ans = 0
for i in range(keta_min, 20):
    if i > keta_max:
        break
    if i == keta_min:
        count = (10 ** i - L)
        ans += (10 ** i + L - 1) * count * i // 2
        ans %= mod

    elif i == keta_max:
        count = (R - 10 ** (i - 1) + 1)
        ans += (R + 10 ** (i - 1)) * count * i // 2

    else:
        count = (10 ** i - 10 ** (i - 1))
        ans += ((10 ** i)- 1 + (10 ** (i - 1))) * count * i // 2
        ans %= mod


print(ans % (10**9 + 7))