N = int(input())
S = input()
count_T = 0
count_A = 0
flag = S[-1]
for i in range(N):
    if S[i] == "A":
        count_A += 1
    else:
        count_T += 1

if count_A == count_T:
    if flag == "A":
        print("T")
    else:
        print("A")
elif count_A > count_T:
    print("A")
else:
    print("T")