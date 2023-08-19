S = input().split()
T = input().split()

count = 0
for i in range(3):
    if S[i] != T[i]:
        count += 1

if count == 2:
    print("No")
else:
    print("Yes")
