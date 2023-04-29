K = int(input())

if K >= 60:
    print("{}:{:0>2}".format(22,K-60))
else:
    print("{}:{:0>2}".format(21,K))