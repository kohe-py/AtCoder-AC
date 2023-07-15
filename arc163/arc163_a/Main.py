from collections import defaultdict
for _ in range(int(input())):
    flag = False
    N = int(input())
    S = input()
    tmp = ""
    for i in range(N):
        tmp += S[i]
        result = ""
        if flag:
            break
        for j in range(i + 1, N):
            result += S[j]
            if j - i - 1 <= i and ord(result[j - i - 1]) < ord(tmp[j - i - 1]):
                break
            elif j - i - 1 <= i and ord(result[j - i - 1]) > ord(tmp[j - i - 1]):
                flag = True
                break
            elif j - i - 1 == i and ord(result[j - i - 1]) == ord(tmp[j - i - 1]):
                if j < N - 1:
                    flag = True
                    break

    if flag:
        print("Yes")
    else:
        print("No")
