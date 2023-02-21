##To check a whether a number is prime or not


num=int(input("Enter the number you want to check:"))
count=0

if num>1:
    for i in range(1,num+1):
        if (num%i)==0:
            count=count+1
    print(count)
    if count==2:
        print("The given number is prime")
    else:
        print("The number is not prime")


