#1
def greet():
    print("hello world!")

greet()

#2
def greet(name):
    print(f"hello, {name}!")

greet("Zombie")

#3
def square(number):
    return number ** 2
result = square(5)
print(result)

#4
def is_even(number):
    return number % 2 == 0

print(is_even(4))
print(is_even(7))

#5
def print_number(n):
    for i in range(1, n + 1):
        print(i)
print_number(5)


