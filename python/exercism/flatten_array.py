def flatten(iterable):
    flattened = []

    for num in iterable:
        if type(num) == list:
            print("else")
            flattened.extend(flatten(num))
        elif type(num) == int:
            flattened.append(num)

    return flattened


print(flatten([0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]))
print(type([]))