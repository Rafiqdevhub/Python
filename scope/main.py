# name="Muhammad Ali"

# def main(full_name="Muhammad Ali Ik"):
#     print(name)
#     print(full_name)

# main("Muhammad Ali Mughal")
# main("Muhammad Ali khan")

# def greet():
    # main("Muhammad Ali Mughal")
#     main()

# greet()

name="Muhammad Ali"
count=0

def value():
    color="red"
    global count
    count+=1
    print(count)

    def inner():
        nonlocal color
        color="blue"
        color="green"
        print(color)
        print(name)
    inner()

value()