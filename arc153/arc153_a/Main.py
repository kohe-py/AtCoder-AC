N = int(input())
s = "100000000"
count = 0
flag = False
for i in range(1,10):
    if flag:
        break
    for j in range(0,10):
        if flag:
            break
        for k in range(0, 10):
            if flag:
                break
            for l in range(0,10):
                if flag:
                    break
                for m in range(0, 10):
                    if flag:
                        break
                    for n in range(0, 10):
                        count += 1
                        if count == N:
                            ans = [i,j,k,l,m,n]
                            flag = True
                            break

#print(ans)
result = str(ans[0]) + str(ans[0])+ str(ans[1]) + str(ans[2]) + str(ans[3]) + str(ans[3]) + str(ans[4]) + str(ans[5]) + str(ans[4])
print(int(result))