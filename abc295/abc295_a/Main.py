N = int(input())
W = list(map(str, input().split()))

l = {"and", "not", "that", "you", "the"}
for i in W:
    if i in l:
        print("Yes")
        exit()
print("No")