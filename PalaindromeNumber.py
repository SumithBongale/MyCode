number = int(input("Enter the Number"))
value=number
sum=0
while value>0:
    k=value%10
    sum=sum*10+k
    value=value//10
if sum==number:
    print("Number is a palindrome")
else:
    print("Number is not a palindrom")
