S = input()

from collections import defaultdict
d = defaultdict(list)
for i in range(len(S)):
    d[S[i]].append(i)

if d["B"][0] % 2 != d["B"][1] % 2:
    if d["R"][0] < d["K"][0] < d["R"][1]:
        print("Yes")
        exit()
print("No")