S = input()
N = int(input())

result = 0
s = []
leng = len(S)
for i in range(leng):
    if S[i] == "1":
        result += 2**(leng - 1 - i)
    elif S[i] == "?":
        s.append(leng - i - 1)

if result > N:
    print(-1)
    exit()

for i in range(len(s)):
    if result + 2 ** (s[i]) <= N:
        result += 2 ** (s[i])

print(result)