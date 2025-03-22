def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    count = 0
    copy_number = number
    while (copy_number != 1):
        count += 1
        if copy_number % 2 == 0:
            copy_number /= 2
        else:
            copy_number = (copy_number * 3) + 1

    return count

print(steps(0))