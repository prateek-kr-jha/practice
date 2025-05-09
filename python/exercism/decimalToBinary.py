def to_binary(num):
    total_eggs = 0
    while num != 0:
        total_eggs += num % 2
        num //=2

    return total_eggs


print(to_binary(16))