S = input()
T = input()

if len(T) > len(S):
    print("No")
else:
    if T in S:
        print("Yes")
    else:
        print("No")