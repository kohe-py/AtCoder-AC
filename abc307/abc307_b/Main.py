N = int(input())
S = [input() for _ in range(N)]

ans = [0] * N
for i in range(N):
    for j in range(N):
        lengi = len(S[i])
        lengj = len(S[j])
        if i != j:
            s = S[i] + S[j]
            count = 0
            for k in range((lengi + lengj) // 2):
                if s[k] != s[-1-k]:
                    break
                else:
                    count += 1
                if count == (lengi + lengj) // 2:
                    print("Yes")
                    exit()

print("No")