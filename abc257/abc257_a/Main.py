N, X = map(int, input().split())
if X % N == 0:
    print(chr(ord("A") - 1 + (X // N)) )
else:
    print(chr(ord("A") + (X // N)))