def prime_no(value):
    sum = 0
    while value > 0:
        k = value%10
        sum = sum*10 + k
        value = value//10
    return sum


number = int(input("Enter the number"))
if prime_no(number) == number:
    print("palindrome number")
else:
    print("Not a palindrome number")
