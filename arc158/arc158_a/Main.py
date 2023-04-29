T = int(input())
for _ in range(T):
    x, y, z = map(int, input().split())
    sum = x + y + z
    if x == y == z:
        print(0)
       
    elif x % 2 == y % 2 == z % 2 and sum % 3 == 0:
        count = 0
        sum //= 3
        x -= sum
        y -= sum
        z -= sum
        list = [x, y, z]
        for i in list:
            count += abs(i)
        print(count//4)

    else:
        print(-1) 