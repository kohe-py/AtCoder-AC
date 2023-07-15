def base10toN(number, n):
    result = ""
    while True:
        x = number % n
        result = str(x) + result
        number //= n
        if number == 0:
            break
    return result
from collections import defaultdict
for _ in range(int(input())):
    N, K = map(int, input().split())
    result = base10toN(N, 3)
    count_min = 0
    count_max = 0
    leng = len(result)
    j = 0
    first = 0
    flag = defaultdict(int)
    for i in reversed(range(leng)):
        flag[(int(result[i]))] += 1
        if j == 0:
            first = int(result[i])
            flag[int(result[i])] -= 1
        count_min += int(result[i])
        count_max += int(result[i]) * (3 ** j)
        j += 1
        
    #print(result, count_min)
    k = K - first
    count_max -= first
    if count_min > K or N < K:
        print("No")
    elif K == N:
        print("Yes")
    else:
        if N % 2 == K % 2:
            print("Yes")
        else:
            print("No")