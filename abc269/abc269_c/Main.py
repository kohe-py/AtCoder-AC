N = int(input())
n = bin(N)
s = []
count = 0
for i in range(len(n)):
    if n[-1 - i] == "b":
        break
    elif n[-1 -i] == "1":
        s.append(i)
        count += 1
ans = []
for bit in range(2 ** count):
    result = 0
    for i in range(count):
        if ((bit >> i) & 1):
            result += 2 ** s[i]
    ans.append(result)

ans.sort()
print(*ans, sep="\n")