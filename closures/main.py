def outer():
    message = "Hello World"
    def inner():
        print(message)  
    return inner

my_func = outer()
my_func() 



def counter():
    count = 0
    def inc():
        nonlocal count  
        count += 1
        return count
    return inc

c = counter()
print(c())  
# print(c()) 
# print(c()) 
# print(c()) 
# print(c()) 
# print(c()) 
# print(c()) 

print("The end fo Closures")


def multiplier(n):
    def inner(x):
        return x * n
    return inner

times3 = multiplier(3)
print(times3(5)) 
print(times3(2)) 
print(times3(1)) 