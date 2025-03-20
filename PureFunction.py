#Map
MY_LIST = [1, 2, 3, 4, 5]
def multiply_by2(item):
    return item*2

map_result = map(multiply_by2, MY_LIST)
print(list(map_result))
#putput: [2, 4, 6, 8, 10]

print(list(map(lambda x: x*2, MY_LIST)))
#using lambda function
#output: [2, 4, 6, 8, 10]




#Filter
def only_odd(item):
    return item % 2 != 0

filter_result = filter(only_odd, MY_LIST)
print(list(filter_result))
#output: [1, 3, 5]

print(list(filter(lambda x: x % 2 != 0, MY_LIST)))
#using lambda function
#output: [1, 3, 5]




#Zip
MY_LIST2 = [6, 7, 8, 9, 10]
zip_result = zip(MY_LIST, MY_LIST2)
print(list(zip_result))
#output: [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]




#Reduce
from functools import reduce #reduce is not a built-in function in python3 need to import it from functools

def accumulator(acc, item):
    return acc + item

reduce_result = reduce(accumulator, MY_LIST, 0)
print(reduce_result)
#accumulator(0, 1) -> 1
#accumulator(1, 2) -> 3
#accumulator(3, 3) -> 6
#accumulator(6, 4) -> 10
#accumulator(10, 5) -> 15s
#output: 15

print(reduce(lambda acc, item: acc + item, MY_LIST, 0))
#using lambda function
#output: 15