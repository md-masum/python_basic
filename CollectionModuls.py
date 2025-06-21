from collections import Counter, defaultdict, OrderedDict
import pdb


def double(x):
   breakpoint() # Set a breakpoint for debugging
   return x * 2
val = 3
print(f"{val} * 2 is {double(val)}")

# Counter example
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(Counter(list))  # Count occurrences of each element
#output: Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1})

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]
print(Counter(list2))  # Count occurrences of each element
#output: Counter({1: 2, 2: 2, 3: 2, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1})


# defaultdict example
dd = defaultdict(int)
for char in "hello world":
    dd[char] += 1
print("defaultdict:", dict(dd))  # Output: defaultdict: {'h': 1, 'e': 1, 'l': 3, ...}

# OrderedDict example
od = OrderedDict()
od["banana"] = 3
od["apple"] = 4
od["orange"] = 2
print("OrderedDict:", od)  # Output: OrderedDict([('banana', 3), ('apple', 4), ('orange', 2)])