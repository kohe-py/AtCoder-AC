S = input()
T = input()

from collections import Counter, defaultdict
counts = Counter(S)
countt = Counter(T)
check = {"a", "t", "c", "o", "d", "e", "r"}

ats = counts["@"]
att = countt["@"]
count = 0

for i in counts.keys():
    if i not in check and i != "@":
        if i in countt and countt[i] != counts[i]:
            print("No")
            exit()
        if i not in countt:
            print("No")
            exit()
    else:
        pass

for i in check:
    if countt[i] > counts[i]:
        ats -= (countt[i] - counts[i])
    else:
        att -= (counts[i] - countt[i])
    if att < 0 or ats < 0:
        print("No")
        exit()

for i in countt.keys():
    if i not in check and i != "@":
        if i in counts and countt[i] != counts[i]:
            print("No")
            exit()
        if i not in counts:
            print("No")
            exit()
    else:
        pass

print("Yes")