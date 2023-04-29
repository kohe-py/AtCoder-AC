hw = list(map(int, input().split()))

# a b c   c = hw[0] - b - a
# d e f
# g h i 
nlist = list(range(1, 31))
nset = set(nlist)
count = 0
for a in range(1, 31):
    for b in range(1, 31):
        for d in range(1, 31):
            for e in range(1, 31):
                c = hw[0] - a - b
                f = hw[1] - d - e
                g = hw[3] - a - d
                h = hw[4] - b - e
                i = hw[2] - g - h
                j = hw[5] - c - f
                #print({c,f,g,h,i})
                if i == j and c in nset and f in nset and g in nset and h in nset and i in nset:
                    count += 1
print(count)