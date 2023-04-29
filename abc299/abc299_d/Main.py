N = int(input())
i = 0
result = -1
left = 1
right= N
zero = 1
one = N
from collections import defaultdict
d = defaultdict(int)
d[1] = 0
d[N] = 1
s = set()
for i in range(20):
    center = left + (right - left) // 2
    print("?", center)
    ans = int(input())
    s.add(center)
    d[center] = ans
    if i == 0:
        if ans == 1:
            right = center
        else:
            left = center
    else:
        if ans == 1:
            if zero < center:
                right = center
            else:
                left = center
        else:
            if one < center:
                right = center
            else:
                left = center
    
    if ans == 1:
        if abs(center - zero) < abs(one - zero):
            one = center
    else:
        if abs(center - one) < abs(zero - one):
            zero = center
    
    if center + 1 in s and d[center+1] != d[center]:
        print("!", center)
        exit()
    if center - 1 in s and d[center - 1] != d[center]:
        print("!", center - 1)
        exit()
            
print("!", center)
            