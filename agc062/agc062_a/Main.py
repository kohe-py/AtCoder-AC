T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    result = S.count("A")
    if result == N:
        print("A")
    elif result == 0:
        print("B")
    else:
        if result == N - 1:
            if S[-1] == "B":
                print("B")
            else:
                print("A")
        else:
            count = 0
            b = N - result
            for i in range(b):
                if S[-1-i] == "B":
                    count += 1
            if count == b:
                print("B")
            else:
                print("A")