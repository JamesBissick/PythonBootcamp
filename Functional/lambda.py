# Lambda expression are like ternary operator and anonymous functions in js
# the operation is declared inside the lambda itself, not another func
my_list = [1, 2, 3, 4, 5]

# def multiply_by2(item):
#     return item * 2


print(list(map(lambda item: item * 2, my_list)))

# Ex1: Square each numbers of the list using lambda
my_list2 = [4, 5, 3]

print(list(map(lambda num: num * num, my_list2)))

# Ex2: List sorting of tuples
# Sort the list a by its second number of each tuples
a = [(10, -4), (9, 9), (4, 3), (0, 2)]

a.sort(key=lambda num: num[1])
print(a)
