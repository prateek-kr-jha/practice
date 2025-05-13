print("A".center(5, '.'))

def rows(letter):
    diff = ord(letter) - ord("A")
    curr = "A"
    diamond = []

    for i in range(0, diff + 1):
        curr_diff = ord(letter) - ord(curr)

        print_str = ""
        for j in range(0, 2 * diff + 1):
            if j == curr_diff or j == 2 * diff - curr_diff:
                print_str += curr
            else:
                print_str += "."


        diamond.append(print_str)
        curr = chr(ord(curr) + 1)

    diamond.extend(diamond[:-1][::-1])
    return diamond

print(rows("A"))