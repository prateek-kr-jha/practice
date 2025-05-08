SUBLIST = None
SUPERLIST = None
EQUAL = None
UNEQUAL = None

def is_sublist(smaller, larger):
    m, n = len(smaller), len(larger)

    if m == 0:
        return True
    
    for i in range(n - m + 1):
        if larger[i: i + m] == smaller:
            return True
    
    return False
            



def sublist(list_one, list_two):
    if list_one == list_two:
        EQUAL = 1
    else:
        UNEQUAL = 1


# B = [1, 2, 3, 4, 5]
# A = [3, 4]
# A = []
# B = []

# print([1, 2, 3] == [1, 2, 3, 4])

# Equal = same values in same order
# Superlist = if A contains contiguous sub-sequence in B
# Sublist = if B contains contiguous sub-sequence in A
# Unequal  =
print(is_sublist([4, 5], [1, 2, 3, 4]))


# naive: sliding window
# naive: use any(generator)
# knuth-morris-pratt (KMP)