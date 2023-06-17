N = int(input())

n = str(N)
leng = len(n)
_list = []
for i in range(leng):
    _list.append(int(n[i]))

leng = len(n)
ans = -1
for bit in range(2 ** leng):
    left = []
    right = []
    count = 0
    for i in range(leng):
        if ((bit >> i) & 1):
            left.append(_list[i])
            count += 1
        else:
            right.append(_list[i])

    left = sorted(left, reverse=True)
    right = sorted(right, reverse=True)
    l, r = 0, 0
    for j in range(count):
        l += left[j] * (10 ** (count - j - 1))
    for j in range(leng - count):
        r += right[j] * (10 ** (leng - count - j - 1))
    ans = max(ans, l * r)

print(ans)