KEY="abcdefghijklmnopqrstuvwxyz"

def encode(plain_text):
    cleaned_text = plain_text.lower().replace(" ", "").replace(",", "").replace(".", "")
    encoded = ""

    for i, char in enumerate(cleaned_text):
        idx = KEY.find(char)
        encoded += KEY[25 - idx] if idx != -1 else char
        if (i + 1) % 5 == 0 and i != len(cleaned_text) - 1:
            encoded += " "

    return encoded

def decode(ciphered_text):
    cleaned_text = ciphered_text.replace(" ", "")
    decoded = ""
    for char in cleaned_text:
        idx = KEY.find(char)
        decoded += KEY[25 - idx] if idx != -1 else char

    return decoded

print(encode("Testing,1 2 3, testing."))
print(decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"))