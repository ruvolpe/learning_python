#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("I am a function")

func1()
print(func1())
print(func1)

# TODO: function that takes arguments
def func2(arg1, arg2):
    print(arg1, arg2)

func2(1, 2)

# TODO: function that returns a value
def cube(x):
    return x * x *x
print(cube(3))

# TODO: function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print(power(2, 4))
print(power(x=2, num=5))

# TODO: function with variable number of arguments

def multi_add(*args):
    result = 0
    for x in args:
        result += x
    return result

print(multi_add(1,2,3))


