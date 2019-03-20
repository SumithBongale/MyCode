number=int(input("Enter the number to check"))
value=number
sum=0
for i in range(1,value//2+1):
    if value % i==0:
        sum=sum+i
    else:
        continue
if sum==number:
    print("{} is perfect number".format(number))
else:
    print("{} is not a perfect number".format(number))
