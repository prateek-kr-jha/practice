from stack import Stack

def revString(string):
    s = Stack()
    for ch in string:
        s.push(ch)
    revStr = ""

    while not s.is_empty():
        revStr += s.pop()
    
    return revStr

print(revString("hello"))
