N = int(input())
S = input()

ans = S.count("OX")
SS = list(S)
for i in range(N - 1):
    if SS[i] + SS[i + 1] == "OX":
        SS[i] = ""
        SS[i + 1] = ""
result = ""
for i in range(N):
    result += SS[i]

ans += result.count("XO")
#print(SS)
print(ans)