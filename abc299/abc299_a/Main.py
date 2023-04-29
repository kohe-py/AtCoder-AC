N = int(input())
S = input()

l = []
ten = []
for i in range(N):
    if S[i] == "|":
        l.append(i)
    if S[i] == "*":
        ten.append(i)

if l[0] <= ten[0] <= l[1]:
    print("in")
else:
    print("out")