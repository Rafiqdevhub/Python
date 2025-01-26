value= 1

# while value <=10:
#     print(value)
#     if value == 5:
#         break
#     value += 1
# print("End of the loop")

# Continue statement in a loop (to escape a certain condition)

# while value <=10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("End of the loop " + str(value))

# while value <=10:
#     value *= 2
#     if value == 8:
#         continue
#     print(value)


# for loop

# for name in names:
names= ["Ahmed ", "Ali", "Omar", "Sara", "Nada", "Hassan"]
#     print(name)

# for name in names:
# for letter in "Python":
#     print(letter)

# for name in names:
#     if name == "Sara":
#         print("Found  " + name + " and the loop will break")
#         break
#     print(name)

# for name in names:
#     if name == "Sara":
#         print("Found  " + name + " and and the loop will continue")
#         continue
    # print(name)

# for name in range(1, 10):
#     print(name)


# for name in range(1, 10, 2):
#     print(name)
# else:
#     print("End of the loop")


names= ["Ahmed ", "Ali", "Omar", "Sara", "Nada", "Hassan"]
occuptions= ["Doctor", "Engineer", "Teacher", "Nurse", "Pilot", "Lawyer"]

# for name in names:
#     for occuption in occuptions:
#         print(name + " is a " + occuption)

for occuption in occuptions:
    for name in names:
        print(name + " is a " + occuption)

# for name, occuption in zip(names, occuptions):
#     print(name + " is a " + occuption)
