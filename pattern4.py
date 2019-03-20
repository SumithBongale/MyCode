row = int(input("Enter the row"))
k=2*row-2
for i in range(1,row):
    for k in range(0,k):
        print(end=' ')
    k=k-1
    for j in range(1,i+1):
        print('*',end=' ')
    print("\r")
