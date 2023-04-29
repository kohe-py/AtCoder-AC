def main():
    n = int(input())
    s = ''

    def dfs(s):
        ret = 0
        numbers = ['3', '5', '7']

        if len(s) > 0:
            if int(s) > n:
                return ret
            else:
                ok = True
                for c in numbers:
                    if s.find(c) == -1:
                        ok = False
                if ok:
                    ret += 1

        for c in numbers:
            s += c
            ret += dfs(s)
            s = s[:-1]

        return ret

    return dfs(s)


if __name__ == '__main__':
    print(main())