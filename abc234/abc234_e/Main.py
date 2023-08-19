X = int(input())

x = str(X)
for a in range(1, 10): # 初項a
    for d in range(-9, 10): # 公差がdの時を考える
        tmp = [str(a)]
        if a + (len(x) - 1) * d < 0 or a + (len(x) - 1) * d >= 10:
            continue
        for i in range(len(x) - 1):
            tmp.append(str(int(tmp[-1]) + d))
        result = "".join(tmp)
        if int(result) >= X:
            print(result)
            exit()