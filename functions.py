# function are the group of statements are together perform a specific task
# function formation


def func(Name, Age):
    print(Name, Age)


func("jojo", 21)
# printing the arguments


def func1(*args):
    for i in args:
        print(i)


func1(20, 40, 60)
func1(80, 100)
# return statement.


def code(a, b):
    return a+b, a-b


res = code(40, 10)
print(res)
#Recursion in python
def display(num):
    if num == 10:
        return 
    display(num+1)
    print(num)

display(5)