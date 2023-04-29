a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
b = ["a", "b", "c", "d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
N = input()

T = ""
for i in range(len(N)):
    for j in range(len(a)):
        if N[i] == b[j]:
            T += a[j]
            break
print(T)