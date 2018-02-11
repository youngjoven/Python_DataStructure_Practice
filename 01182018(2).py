def a():
    print(5*7)
a()


def b(x,y):
    print(x*y)
print(b(1,2))


def c():
    return(5*7)
product = c()
print(c())
print(product)


def d(x,y):
    return(x*y)
d(6,5)


def car(name, wheel=4, fuel="gasoline"):
    print("Name :", name, "/ Wheel :",wheel, "/ Fuel :", fuel)
car("Benz")
car("Dump Truck", 6, fuel="disel")

def greetings(*names):
    print(type(names))
    print("Hello, ", end = "")
    for i in range(0, len(names)):
        if i == len(names)-1:
            print(names[i], "!", sep="")
            break
        print(names[i], end=", ")

greetings("John", "Chris", "James")
greetings(1,2,"Kim", [3,4,5])
