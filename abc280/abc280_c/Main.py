S = input()
T = input()

for i in range(len(T)):
    if i == len(T)-1:
        break
    elif S[i] != T[i]:
        break
print(i+1)