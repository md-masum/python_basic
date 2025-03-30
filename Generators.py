# Generators are a simple way to create iterators. They allow you to yield items one at a time as they are needed,
# rather than storing the entire sequence in memory. This is especially useful for large datasets.

# Example: A generator function to yield squares of numbers up to a given limit
def square_numbers(limit):
    for i in range(limit):
        yield i * i  # 'yield' pauses the function and returns the value

# Using the generator
squares = square_numbers(5)  # Create a generator object

# Iterate through the generator
for square in squares:
    print(square)  # Output: 0, 1, 4, 9, 16

# Additional Example: Comparing generator with a list
# Using a list to store squares
squares_list = [i * i for i in range(5)]  # List comprehension
print("List:", squares_list)  # Output: List: [0, 1, 4, 9, 16]

# Using a generator to produce squares
squares_gen = (i * i for i in range(5))  # Generator expression
print("Generator:", list(squares_gen))  # Output: Generator: [0, 1, 4, 9, 16]

# Difference:
# 1. The list stores all values in memory at once, which can be memory-intensive for large datasets.
# 2. The generator produces values on-the-fly, consuming less memory.

# Explanation:
# 1. The `yield` keyword is used to produce a value and pause the function's execution.
# 2. When the generator is iterated, it resumes execution from where it was paused.
# 3. Generators are memory-efficient because they do not store all values in memory at once.



def fibonacci(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

# Using the generator
for num in fibonacci(10):
    print(num)  # Output: 0 1 1 2 3 5 8 13 21 34