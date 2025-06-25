from stack import Stack

def balance_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                if not matches(s.pop(), symbol):
                    return False
        
    return s.is_empty()


def matches(symbol_left, symbol_right):
    all_lefts = "([{"
    all_rights = ")]}"

    return all_lefts.index(symbol_left) == all_rights.index(symbol_right)


print(balance_checker('{({([][])}())}'))
print(balance_checker('[{()]'))
