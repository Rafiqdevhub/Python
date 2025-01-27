def greeting():
    print(f"Hello world!")

greeting()  


# def sum(a, b):
#     return a + b

# print("The sum is:",sum(1, 2))
# print("The sum is:",sum(1, 3))
# print("The sum is:",sum(1, 2))
# print("The sum is:",sum(4, 2))
# print("The sum is:",sum(9, 2))


# def sum(a, b):
#     if type(a) is not int or type(b) is not int:
#        return
#     return a + b

# total = sum(1, 2)
# total = sum(1, 3)
# print("The sum is:",total)
# print("The sum is:",total)

# total = sum(1, "2")
# print("The sum is:",total)


# def sum(num1=0, num2=0):
#     if type(num1) is not int or type(num2) is not int:
#        return
#     return num1 + num2

# total = sum( 2)
# print("The sum is:",total)

# def multiple_items(*args):
#     print(args)
#     print(type(args))

# multiple_items("apple", "banana", "cherry", "date", "elderberry")


# def multiple_items(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# multiple_items(fruit1="apple", fruit2="banana", fruit3="cherry", fruit4="date", fruit5="elderberry")


def multiple_names(*args, **kwargs):
    print(args)
    print(kwargs)
    print(type(args))
    print(type(kwargs))

multiple_names("apple", "banana", "cherry", "date", "elderberry", fruit1="apple", fruit2="banana", fruit3="cherry", fruit4="date", fruit5="elderberry")