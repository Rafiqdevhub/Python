num = int(input("Enter a number: "))
factorial = 1
if num <0:
 print("Factorial does not exist for negative numbers")
elif num == 0:
 print("Factorial of 0 is 1")
else:
 for i in range(1, num+1):
    factorial = factorial*i
#  print(f'The factorial of {num} is {factorial}')



# nterms = int(input("How many terms? "))
#  # first two terms
# n1, n2 = 0, 1
# count = 0
#  # check if the number of terms is valid
# if nterms <= 0:
#  print("Please enter a positive integer")
#  # if there is only one term, return n1
# elif nterms == 1:
#  print("Fibonacci sequence upto",nterms,":")
#  print(n1)
#  # generate fibonacci sequence
# else:
#  print("Fibonacci sequence:")
#  while count < nterms:
#     print(n1)
#     nth = n1 + n2
#  # update values
#     n1 = n2
#     n2 = nth
#     count += 1


 def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
 nterms = int(input("Enter the number of terms (greater than 0): "))
 # check if the number of terms is valid
 if nterms <= 0:
    print("Plese enter a positive integer")
 else:
    print("Fibonacci sequence:")
 for i in range(nterms):
    print(recur_fibo(i))



 def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
 num = int(input("Enter the number: "))
 # check if the number is negative
 if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
 elif num == 0:
    print("The factorial of 0 is 1")
 else:
    print("The factorial of", num, "is", recur_factorial(num))