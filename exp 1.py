num=int(input("Enter a Number: "))
if num%2==0:
    rem=0
    a=num
    while a!=0:
        d = a%10
        rem = d + rem*10
        a //= 10
    if rem==num:
        print("Number is Pallindrome")
    else:
        print("Number is not Pallindrome")
else:
    fact = 1
    for i in range(num,0,-1):
        fact = fact * i
    a = fact
    e = 0
    while a != 0:
        e += 1
        a //= 10
    print("Number of digits in the factorial {} of the number {}".format(fact,e))
