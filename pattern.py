for i in range(0,6):
    print("\n")
    for j in range(0,i):
        if (i+j)%2==0:
            print("0",end='')
        else:
            print("1",end='')
for i in range(0,6):
    print("\n")
    for j in range(0,4-i):
        if (i+j)%2==0:
            print("0",end='')
        else:
            print("1",end='')
