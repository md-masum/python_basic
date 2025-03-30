# Example of Python Collections

# 1. List: Ordered, mutable, allows duplicate elements
# Similar to tuples (ordered) but can be modified. Unlike sets, it allows duplicates.
# Example: A collection of fruits
fruits = ["apple", "banana", "cherry", "apple"]
print("List:", fruits)  # Output: List: ['apple', 'banana', 'cherry', 'apple']

# 2. Tuple: Ordered, immutable, allows duplicate elements
# Similar to lists but immutable. Unlike sets, it allows duplicates.
# Simillar to lists but cannot be modified after creation.
# Example: A collection of coordinates
coordinates = (10, 20, 30, 10)
print("Tuple:", coordinates)  # Output: Tuple: (10, 20, 30, 10)

# 3. Dictionary: Unordered (Python 3.6+ maintains insertion order), mutable, key-value pairs
# Similar to sets but with key-value pairs. Keys must be unique and immutable.
# Example: A collection of student grades
grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("Dictionary:", grades)  # Output: Dictionary: {'Alice': 85, 'Bob': 90, 'Charlie': 78}

# 4. Set: Unordered, mutable, no duplicate elements
# Similar to dictionaries but only with keys. Sets are useful for storing unique items.
# Example: A collection of unique numbers
unique_numbers = {1, 2, 3, 4, 1}
print("Set:", unique_numbers)  # Output: Set: {1, 2, 3, 4}

# 5. Frozenset: Unordered, immutable, no duplicate elements
# Similar to sets but immutable. Frozensets are useful for hashable items, cannot be modified after creation..
# Example: A collection of unique immutable items
immutable_set = frozenset([1, 2, 3, 4, 1])
print("Frozenset:", immutable_set)  # Output: Frozenset: frozenset({1, 2, 3, 4})

# 6. String: Ordered, immutable, sequence of characters
# Similar to tuples but specifically for characters. Strings are immutable.
# Example: A collection of characters
text = "Hello, World!"
print("String:", text)  # Output: String: Hello, World!

# 7. Byte: Immutable sequence of bytes
# Similar to strings but specifically for bytes. Bytes are immutable.
# Example: A collection of bytes
byte_data = b"Hello"
print("Byte:", byte_data)  # Output: Byte: b'Hello'

# 8. Bytearray: Mutable sequence of bytes
# Similar to bytes but mutable. Bytearrays can be modified after creation.
# Example: A mutable collection of bytes
mutable_byte_data = bytearray(b"Hello")
mutable_byte_data[0] = 74  # Changing the first byte
print("Bytearray:", mutable_byte_data)  # Output: Bytearray: bytearray(b'Hello')

# 9. Range: Immutable sequence of numbers
# Similar to lists but specifically for numbers. Ranges are immutable.
# Example: A range of numbers
number_range = range(1, 10, 2)
print("Range:", list(number_range))  # Output: Range: [1, 3, 5, 7, 9]