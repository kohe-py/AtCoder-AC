from collections import defaultdict
N = int(input())
d = defaultdict(int)

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
ans = 0
for ab in range(1, N):
    cd = N - ab
    #print(make_divisors(ab), make_divisors(cd))
    if d[ab] == 0:
        d[ab] = len(make_divisors(ab))
    if d[cd] == 0:
        d[cd] = len(make_divisors(cd))
        
    if d[ab] == 1 and d[cd] != 1:
        ans += d[cd]
    elif d[cd] == 1 and d[ab] != 1:
        ans += d[ab]
    elif d[cd] == 1 and d[cd] == 1:
        ans += 1
    elif d[cd] != 1 and d[ab] != 1:
        ans += (d[ab] * d[cd])
    #print(ans)
print(ans)