# A decorator in Python is a function that takes another function (or method) as an argument and extends or modifies its behavior without modifying its actual code.

# def create_ice(func):
#     def wrapper():
#         print("Ice created!")
#         func()
#         print("Ice is ready!")
#     return wrapper

# @create_ice
# def create_cream():
#     print("Cream created!")
    
# create_cream()

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Function is being called")
#         result = func(*args, **kwargs)
#         print("Function execution finished")
#         return result
#     return wrapper

# @my_decorator
# def add(a, b):
#     print("The result is: ", a+b)
    
# print(add(2, 3))

import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper

@log_time
def slow_function():
    time.sleep(2)
    print("Function finished")

slow_function()

