#11
x = 10
def print_x():
    x = 20
    print(f"local x: {x}")
print(x)
print(f"Global x: {x}")

#12
count = 0
def increment():
    global count
    count += 1
    print(f"Count: {count}")

increment()
increment()
print(f"Final count: {count}")

#13
def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"
        print(f"Inner x: {x}")
    inner()
    print(f"outer x: {x}")
outer()

#14
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

#15
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(7))

