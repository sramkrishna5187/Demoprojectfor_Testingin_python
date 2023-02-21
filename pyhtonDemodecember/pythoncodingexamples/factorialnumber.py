
factorial=1
num=5
if num<0:
    print("The factorial for negative numbers does not exist")
elif num==0:
    print("The factorial for the number is 1")
else:
    for i in range(1,num+1):
        factorial =factorial*i
    print("The factorial for the given number is: ",factorial)
# */******************************
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    # terenary operator
    return 1 if (n==1 or n==0) else n*factorial(n-1)