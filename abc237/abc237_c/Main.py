S = input()
leng = len(S)
count = 0
for i in range(leng):
    if S[-i-1] == "a":
        count += 1
    else:
        break
for i in range(leng):
    if S[i] == "a":
        count -= 1
    else:
        break

if count < 0:
    exit(print("No"))
if count == 0:
    for i in range(leng // 2):
        if S[i] != S[-i-1]:
            exit(print("No"))
    exit(print("Yes"))
else:
    S = "a" * count + S
    for i in range((leng + count) // 2):
        if S[i] != S[-i-1]:
            exit(print("No"))
    exit(print("Yes"))