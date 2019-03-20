row = int(input("Enter the row"))
for i in range(1,row+1):
    for k in range(0,row-i):
        print(' ',end=' ')
    for j in range(1,i+1):
        print('*',end=' ')
    print()
