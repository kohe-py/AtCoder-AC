N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())


for i in range(P, Q+1):
    result = ""
    for j in range(R, S+1):
        if (i - j == A - B) or (i + j == A + B):
            result += "#"
        else:
            result += "."
    print(result)