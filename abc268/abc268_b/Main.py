S = input()
T = input()

if len(S)>len(T):
    print("No")
    exit()
for i in range(len(S)):
    if T[i] != S[i]:
        print("No")
        exit()
print("Yes")