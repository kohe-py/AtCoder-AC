N=int(input())
x=hex(N)
x=x[2:]
x=x.upper()
print("{:0>2}".format((x)))