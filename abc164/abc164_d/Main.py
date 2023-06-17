S = input()

# len(S) 2 * 10 ^5
# 3 × 673
leng = len(S)


from collections import defaultdict
d = defaultdict(int)
d[0] = 1
now = 0
mod = set()
for i in range(leng):
    now += int(S[-1-i]) * pow(10, i, 2019)
    now %= 2019
    d[now] += 1


ans = 0
for k in d.keys():
    ans += (d[k] - 1) * (d[k]) // 2

print(ans)