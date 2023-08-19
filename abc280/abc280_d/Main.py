K = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5//1)+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

def binary_search(result):
    left = 1
    right = 10 ** 12 + 1
    while abs(right - left) > 1:
        center = left + (right - left) // 2
        if cheack(center, result):
            right = center
        else:
            left = center
    return right


result = factorization(K)
def cheack(center, result):
    for num, count in result:
        flag = 0
        x = center
        while x > 1:
            flag += x // num
            x //= num
        if flag < count:
            return False
    return True

print(binary_search(result))