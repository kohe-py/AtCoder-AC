S = input()
c = 0
for i in range(len(S)):
    if S[i] == "a":
        c = i+1
if c == 0:
    print(-1)
else:
    print(c)