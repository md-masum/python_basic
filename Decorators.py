# Example of a basic decorator in Python

# Decorators are a way to modify or extend the behavior of functions or methods without changing their code.
# Decorators are usually called before the definition of a function you want to decorate.

# import the time module
import time


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'It took {t2-t1} seconds')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i*5

# Call the decorated function
long_time()