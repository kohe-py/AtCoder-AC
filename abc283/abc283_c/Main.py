c = ["1","2","3","4","5","6","7","8","9", "0", "00"]

S = int(input())
T = str(S)
count = 0
while T !=  "":
    h = int(T[len(T)-1:])
    h2 = int(T[len(T)-2:])
    if h2 == 0:
        T = T[:len(T)-2]
        count+=1
    else:
        T = T[:len(T)-1]
        count+=1
print(count)