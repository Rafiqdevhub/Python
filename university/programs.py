# num1=float(input("Enter the first number: "))
# num2=float(input("Enter the second number: "))

# if num2==0:
#     print("The second number cannot be zero")
# else:
#     division=num1/num2
#     print("The division of the two numbers is: ",division)

import random

print(f"Random number: {random.randint(1, 100)}")

# kilometers = float(input("Enter value in kilometers: "))

# conversion_factor = 0.621371

# miles = kilometers * conversion_factor

# print(f"{kilometers} kilometers is equal to {miles} miles")

# celsius = float(input("Enter temperature in celcius: "))

# fahrenheit = (celsius * 9/5) + 32

# print(f"{celsius}°C is equal to {fahrenheit}°F")

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))     

print(calendar.month(year, month))