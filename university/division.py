num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))

if num2==0:
    print("The second number cannot be zero.")

else:
    division=num1/num2
    print("The division of {0} and {1} is {2}".format(num1,num2,division))