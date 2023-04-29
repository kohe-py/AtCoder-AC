N = int(input())
S = input()

start = S[0]
if S[0] == "F":
    for i in range(N):
        if i % 2 == 0:
            if S[i] == "F":
                pass
            else:
                print("No")
                exit()
        else:
            if S[i] == "M":
                pass
            else:
                print("No")
                exit()
else:
    for i in range(N):
        if i % 2 == 1:
            if S[i] == "F":
                pass
            else:
                print("No")
                exit()
        else:
            if S[i] == "M":
                pass
            else:
                print("No")
                exit()
print("Yes")