def Swap(i):
    p[i], p[i+1] = p[i+1], p[i]
    ans.append(i)

def Swap2(i):
    if i % 2 == 0 and i >= 4:
        Swap(1)
    elif i % 2 == 1 and i >= 5:
        Swap(2)
    else:
        Swap(i+1)

for _ in range(int(input())):
    N = int(input())
    p = [-1]+list(map(int, input().split()))

    ans = []
    for n in range(N, 0, -1):
        if n >= 4:
            index = p.index(n)
            if index == n:
                continue
            if n == 4 and index == 3:
                while p[n] != n:
                    if len(ans) % 2 == 0:
                        Swap(3)
                        if p[n] == n:
                            break
                    if len(ans) % 2 == 1:
                        Swap(2)
            elif len(ans) % 2 == 0:
                if index % 2 == 0:
                    Swap2(index)
                while index != n:
                    Swap(index)
                    index += 1
            else:
                if index % 2 == 1:
                    Swap2(index)
                while index != n:
                    Swap(index)
                    index += 1
        elif n == 3:
            while p[1:4] != [1, 2, 3]:
                if len(ans) % 2 == 0:
                    Swap(1)
                    if p[1:4] == [1, 2, 3]:
                        break
                if len(ans) % 2 == 1:
                    Swap(2)
        else:
            if p[1] == 2:
                Swap(1)

    print(len(ans))
    print(*ans)