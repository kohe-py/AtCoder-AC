N = int(input())
c = input()
if c.count("R") == N or c.count("W") == 0:
    print(0)
    exit()
    
ans = min(c.count("R"), c.count("W"))
count = 0
for i in range(c.count("R")):
    if c[i] == "R":
        count += 1
print(min(c.count("R") - count, ans))