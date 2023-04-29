N = int(input())

if N % 2 == 1:
    print()
    exit()

import itertools

def check(data, N):
    start = 0
    end = 0
    for i in range(N):
        if data[i] == "(":
            start += 1
        else:
            end += 1
        if start >= end:
            pass
        else:
            return False
    if start == end:
        return True
    return False


nlist = ["(", ")" ]
ans = []
for i in itertools.product(nlist, repeat=N):
    if check(i, N):
        ans.append("".join(i))

ans.sort()
print(*ans, sep="\n")