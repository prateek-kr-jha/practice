def invalid_isbn(cleaned_isbn):
    return not (len(cleaned_isbn) == 10 and (cleaned_isbn[-1].isdigit() or cleaned_isbn[-1] == "X") and cleaned_isbn[:-1].isdigit())

def is_valid(isbn):
    cleaned_isbn = "".join(isbn.strip().split("-"))
    if invalid_isbn(cleaned_isbn):
        print("invalid")
        return False
    return sum(
        10 if digit == "X" else int(digit) * (10 - i)
        for i, digit in enumerate(cleaned_isbn)
    ) % 11 == 0
        



print(is_valid("3-598-21508-A"))