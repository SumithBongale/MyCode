def prime_no(n):
    for i in range(2,n):
        if n%i==0:
            flag = 0
            break
        else:
            flag = 1
    return flag


if prime_no(7) == 0:
    print("Not a prime number")
else:
    print("Prime number")
