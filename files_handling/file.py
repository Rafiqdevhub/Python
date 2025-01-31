import os
# Read the file

f=open("names.txt","r")

# print(f.read())

# print(f.readline())

# print(f.readline())

# print(f.readline())

# for line in f:
#     print("\nThe name:",line, "\n")
    
# f.close()

try:
    # f=open("names_list.txt","r")
    f=open("names.txt","r")
    print(f.read())
except FileNotFoundError:
    print("The file does not exist")
finally:
    f.close()
    

f=open("names.txt","a")
f.write("\nThis is a new line")
f.close()

f=open("names.txt","r")
print(f.read())
f.close()

f=open("names.txt","w")
f.write("I deleted the previous content")
f.close()

f=open("names.txt","r")
print(f.read())
f.close()

if not os.path.exists("Rafiq.txt"):
    f=open("Rafiq.txt","w")
    f.write("Hello Rafiq")
    f.close()
    

if os.path.exists("Rafiq.txt"):
    os.remove("Rafiq.txt")
    print("The file has been deleted")
else:
    print("The file does not exist")
    
    
with open("names.txt","r") as f:
    print(f.read())

with open("names.txt","w") as f:
    f.write("\nThis is a new line")
    
# if os.path.exists("names.txt"):
#     os.remove("names.txt")
#     print("The file has been deleted")
# else:
#     print("The file does not exist")
    
if os.path.exists("context.txt"):
    os.remove("context.txt")
    print("The file has been deleted")
else:
    print("The file does not exist")