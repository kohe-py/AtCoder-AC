N = int(input())
S = input()

for i in range(N):
    if S[i] == "0":
        pass
    else:
        result = i
        break

if i % 2 == 0:
    print("Takahashi")
else:
    print("Aoki")