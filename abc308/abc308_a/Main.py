S = list(map(int, input().split()))

flag = True
if min(S) < 100:
    print("No")
    exit()
if max(S) > 675:
    print("No")
    exit()

for i in range(len(S)):
    if S[i] % 25 != 0:
        print("No")
        exit()
    if i + 1 < len(S) and S[i] > S[i + 1]:
        print("No")
        exit()
print("Yes")