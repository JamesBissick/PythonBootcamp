some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


def find_duplicates(list):
    duplicates = []
    for item in list:
        if list.count(item) > 1:
            if item not in duplicates:
                duplicates.append(item)
    print(duplicates)


find_duplicates(some_list)
