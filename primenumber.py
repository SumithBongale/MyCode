Number=int(input("enter the number to check"))
flag=1
for i in range(2,Number-1):
    if Number%i == 0:
        flag=0
        break
    else:
        flag=1
if flag==0:
    print("{} is not a prime number".format(Number))
else:
    print("{} is a prime number".format(Number))
