S = list(input())
Q = int(input())

s = []
for i in range(len(S)):
    s.append(ord(S[i]) - 65)

def main(t, k):
    if t == 0:
        return ord(S[k - 1]) - 65
    if k == 1:
        return (s[0] + t) % 3
    elif k % 2 == 0:
        return (main(t - 1, (k // 2))- 1) % 3
    else:
        return (main(t - 1, (k // 2 + 1)) + 1) % 3

for _ in range(Q):
    t, k = map(int, input().split())
    if t == 0:
        print(S[k - 1])
    else:
        print(chr(65 + main(t, k)))