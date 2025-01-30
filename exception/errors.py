class Error_handle(Exception):
    pass

x = 10
try:
    raise Error_handle("An error occurred")
    # print(x)
    # print(x/0)
    # print(x/2)
    # if not type(x) is int:
    if not type(x) is str:
        raise TypeError("Only integers are allowed")
# except:
#     print("An exception occurred")

except NameError:
    print("Variable x is not defined")
    
except ZeroDivisionError:
    print("Any number can't be divided by zero")
    
except Exception as e:
    print(e)
    
else:
    print("No exception occurred")
    
finally:
    print("Finally block executed")