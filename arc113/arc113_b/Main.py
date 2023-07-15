A, B, C = map(int, input().split())

if A == 1:
    exit(print(1))
if A % 10 == 0:
    exit(print(0))
if A % 5 == 0:
    exit(print(5))

# A ** nの一の位の周期をみる
A = A - (A // 10 * 10)
period = []
leng = 0
for i in range(1, 11):
    result = A ** i
    first = result - (result // 10 * 10)
    if first not in period:
        period.append(first)
        leng += 1

#print(period)
# 周期の何回目なのか 
print(period[(pow(B, C, leng)) - 1])