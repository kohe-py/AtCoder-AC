N = int(input())
v = list(map(int, input().split()))

from collections import defaultdict
even = set()
odd = set()
even_dict = defaultdict(int)
odd_dict = defaultdict(int)
for i in range(N):
    if i % 2 == 0:
        even.add(v[i])
        even_dict[v[i]] += 1
    else:
        odd.add(v[i])
        odd_dict[v[i]] += 1

e = []
o = []

if len(set(v)) == 1:
    print(N // 2)
    exit()
    
for i in even_dict.keys():
    e.append((i, even_dict[i]))
for i in odd_dict.keys():
    o.append((i, odd_dict[i]))
e = sorted(e, reverse=True, key=lambda x:x[1])
o = sorted(o, reverse=True, key=lambda x:x[1])

if e[0][0] != o[0][0]:
    print(N - e[0][1] - o[0][1])
else:
    if e[0][1] > o[0][1]:
        print(N - e[0][1] - o[1][1])
    elif e[0][1] == o[0][1]:
        print(N - e[0][1] - max(e[1][1], o[1][1]))
    else:
        print(N - e[1][1] - o[0][1])