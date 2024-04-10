def show1():
    print("This is show1()")

def show2():
    print("This is show2()")

def show3():
    print("This is show3()")

def caller(func):
    func()

# Example usage:
caller(show1)  # Invoking show1()
caller(show2)  # Invoking show2()
caller(show3)  # Invoking show3()
