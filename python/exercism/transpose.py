def transpose(text):
    text2 = [word for word in text.split("\n")]
    sol_str = ""
    # print(text2)
    max_len = max(len(x) for x in text2)

    for text in text2:
        print(text)

    for a in [text + (max_len - len(text)) * " " for text in text2]:
        print(len(a))

    for a in zip(*[list(a) for a in [text + (max_len - len(text)) * " " for text in text2]]):
        for c in a:
            sol_str += c
        sol_str += "\n"
    return sol_str.strip("\n")


print(transpose("The fourth line.\nThe fifth line."))

print("TT\nhh\nee\n  \nff\noi\nuf\nrt\nth\nh \n l\nli\nin\nne\ne.\n." == transpose("The fourth line.\nThe fifth line."))