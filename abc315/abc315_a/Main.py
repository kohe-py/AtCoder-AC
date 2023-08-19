S = input()
s = {"a", "e", "i", "o", "u"}
ans = ""
for i in range(len(S)):
    if S[i] in s:
        continue
    ans += S[i]

print(ans)