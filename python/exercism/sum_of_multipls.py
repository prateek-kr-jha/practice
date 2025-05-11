def sum_of_multiples(limit, multiples):
    
    return sum({
        i
        for num in multiples
        if num != 0
        for i in range(num, limit, num)
    })

print(sum_of_multiples(10, [3, 5]))


