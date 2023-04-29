S = input()
count=0
for s in range(len(S)):
    if S[s] == "v":
        count+=1
    if S[s] == "w":
        count+=2
print(count)