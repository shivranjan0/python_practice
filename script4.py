#check whether the given number is prime or not

a = int(input("Enter a number:"))
if a==1:
    print("it is prime number")
else:
    for i in range(2,a):
        if a%i==0:
            print("it is not a prime number")
            break
        else:
            print("it is prime number")
            break