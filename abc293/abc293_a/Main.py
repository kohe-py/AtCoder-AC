S = list(input())
i = 0
while True:
    if i+1 >= len(S):
        break
    S[i], S[i+1] = S[i+1], S[i]
    #print(i,S)
    i += 2
    
print("".join(S))