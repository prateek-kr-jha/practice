input = [4, 8, 12, 16, 23, 28, 32]

def binary_search(input, target):
    low = 0
    high = len(input) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = input[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def find(search_list, value):
    low = 0
    high = len(search_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if value < search_list[mid]:
            high -= 1
        elif value > search_list[mid]:
            low += 1
        else:
            return mid

    return -1

print(find(input,28))