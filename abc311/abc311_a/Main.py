N = int(input())
S = input()

ans = set()
for i in range(N):
    if S[i] == "A":
        ans.add("A")
    elif S[i] == "B":
        ans.add("B")
    elif S[i] == "C":
        ans.add("C")
    if len(ans) == 3:
        print(i + 1)
        exit()