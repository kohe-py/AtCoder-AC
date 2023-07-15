N = int(input())
S = input()

stack = []
flag = 0
for i in range(N):
    if S[i] == "(":
        flag += 1
    stack.append(S[i])
    if S[i] == ")" and flag >= 1:
        while True:
            v = stack.pop()
            if v == "(":
                flag -= 1
                break
print("".join(stack))