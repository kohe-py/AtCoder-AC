S = input()
str_list = ["dream", "dreamer", "erase", "eraser"]
new_list = []
for i in range(4):
    result = ""
    for j in range(len(str_list[i])):
        result += str_list[i][-1-j]
    new_list.append(result)
#print(new_list)
new_set = set(new_list)

s = ""
for i in range(len(S)):
    s += S[-i-1]
    if s in new_set:
        s = ""
if s == "":
    print("YES")
else:
    print("NO")