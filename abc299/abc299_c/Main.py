N = int(input())
S = input()

flag = False
ans = 1
count = 0
for i in range(N):
    if S[i] == "o":
        count += 1
        flag = True
    else:
        ans = max(ans, count)
        count = 0
c = S.count("o")
if c != N:
    ans = max(ans, count)


if flag == False or c == N:
    print(-1)
else:
    print(ans)