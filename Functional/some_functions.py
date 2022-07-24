# 1.Map
# runs a func then returns an object
def multiply_by2(item):
    return item * 2


print(f'Map object: {map(multiply_by2, [1, 2, 3])}')  # return a map object
print(f'Multiplied list: {list(map(multiply_by2, [1, 2, 3]))}')  # Use List to display the result

# but it doesn't effect the outside world
my_list = [1, 2, 3]
map(multiply_by2, my_list)
print(f'Original list: {my_list}')  # Not affected by map, same output as input

# 2.Filter
# filters things for us
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8]


def only_odd(item):
    return item % 2 != 0


print(f'Odd numbers: {list(filter(only_odd, my_list2))}')
print(f'Original list: {my_list2}')

# 3.Zip
# Takes two lists (or more) and zips them together
my_list3 = [1, 2, 3]
your_list = [60, 70, 80, 90]

print(f'Zipped lists: {list(zip(my_list3, your_list))}')

# 4.Reduce
# Needs to be imported from the functools package
from functools import reduce


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulator, my_list2, 0))
