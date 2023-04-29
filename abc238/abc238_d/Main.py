T = int(input())
for _ in range(T):
    a, s = map(int, input().split())
    if s < a:
        print("No")
    else:
        if a & (s - a) == a:
            print("Yes")
        else:
            print("No")