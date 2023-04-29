a, b = map(int, input().split())
c, d = map(int, input().split())

if a == c and b == d:
    print(0)

elif ((c-a) != 0 and (d-b) / (c-a) in {-1, 1}) or abs(a-c) + abs(b-d) <= 3:
    print(1)

elif abs(a-c) + abs(b-d) <= 6 or (a+b+c+d) % 2 == 0 or abs(a+b-c-d) <= 3 or abs(a-b-c+d) <= 3:
    print(2)
else:
    print(3)
