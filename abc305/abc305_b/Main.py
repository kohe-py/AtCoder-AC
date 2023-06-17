p, q = input().split()

s = [0, 3, 4, 8, 9, 14, 23]
ss = ["A", "B", "C", "D", "E", "F", "G"]

if p < q:
    print(s[ss.index(q)] - s[ss.index(p)])
else:
    print(s[ss.index(p)] - s[ss.index(q)])