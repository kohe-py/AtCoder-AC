S = input()
s = {"ACE", "BDF", "DFA", "CEG", "EGB", "FAC", "GBD"}
for i in s:
    if i == S:
        print("Yes")
        exit()
print("No")