X = input()

if len(set(X)) == 1:
    print("Weak")
    exit()


for i in range(len(X)-1):
    if int(X[i+1]) == int(X[i])+1:
        continue
    elif int(X[i+1]) == 0 and int(X[i]) == 9:
        continue
    else:
        print("Strong")
        exit()
print("Weak")