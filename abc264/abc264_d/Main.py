S = input()
a = "atcoder"
L = [a.index(c) for c in S]
count = 0
for i in range(7 - 1):
    for j in range(7 - i - 1):
        if L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
            count += 1
    
print(count)