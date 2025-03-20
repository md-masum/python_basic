# Comprehensions are a way to build up a list by performing an operation on each item in a sequence.
# The syntax is [expression for item in iterable]
# The expression can be any valid Python expression, including a function call.
# The iterable can be any Python iterable, including a list, tuple, or string.


#Example 1 List Comprehension

MY_LIST = []

for item in 'HELLO':
    MY_LIST.append(item)

print(MY_LIST)
#output: ['H', 'E', 'L', 'L', 'O']

MY_LIST = [item for item in 'HELLO']
print(MY_LIST)
#output: ['H', 'E', 'L', 'L', 'O']

MY_LIST = [item for item in 'HELLO' if item != 'L']
print(MY_LIST)
#output: ['H', 'E', 'O']

MY_LIST = [item if item != 'L' else 'X' for item in 'HELLO']
print(MY_LIST)
#output: ['H', 'E', 'X', 'X', 'O']

MY_LIST = [item for item in range(1, 6)]
print(MY_LIST)
#output: [1, 2, 3, 4, 5]

MY_LIST = [item*2 for item in range(1, 6)]
print(MY_LIST)
#output: [2, 4, 6, 8, 10]




#Example 2 Set Comprehension

MY_SET = {item for item in 'HELLO'}
print(MY_SET)
#output: {'H', 'E', 'L', 'O'} sane as list comprehension but with curly braces




#Example 3 Dictionary Comprehension

MY_DICT = {item: item*2 for item in range(1, 6)}
print(MY_DICT)
#output: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

MY_DICT = {item: item*2 for item in range(1, 6) if item % 2 == 0}
print(MY_DICT)
#output: {2: 4, 4: 8}

MY_DICT = {item: 'even' if item % 2 == 0 else 'odd' for item in range(1, 6)}
print(MY_DICT)
#output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}





#Example 4 Tuple Comprehension

MY_TUPLE = tuple(item for item in range(1, 6))
print(MY_TUPLE)
#output: (1, 2, 3, 4, 5)  same as list comprehension but with parenthesis



#Excercise
SOME_LIST = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
DUPLICATE_LIST = [item for item in SOME_LIST if SOME_LIST.count(item) > 1]
print(DUPLICATE_LIST)
#output: ['b', 'b', 'n', 'n']
DUPLICATE_SET = {item for item in SOME_LIST if SOME_LIST.count(item) > 1}
print(DUPLICATE_SET)
#output: {'b', 'n'}
