num_list = [-8, 2, 3, 4, 8, 15, 9, 12]


def highest_even(list):
    evens = []
    for item in list:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even(num_list))
