##swaping two variables

num1=10
num2=20

print("The value of Num1 before swapping",num1)
print("The value of Num2 before swapping",num2)

num1,num2=num2,num1

print("The value of Num1 After swapping",num1)
print("The value of Num2 After swapping",num2)

temp=num1
num1=num2
num2=temp

print("The value of Num1 After swapping",num1)
print("The value of Num2 After swapping",num2)

num2=num1+num2
num2=num1