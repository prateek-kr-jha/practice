KEY_LOWER = "abcdefghijklmnopqrstuvwxyz"
KEY_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rotate(text, key):
    encoded = ""
    for alphabet in text:
        if alphabet in KEY_LOWER:
            i = KEY_LOWER.index(alphabet)
            rotation = (i + key) % len(KEY_LOWER)
            encoded += KEY_LOWER[rotation]
        elif alphabet in KEY_UPPER:
            i = KEY_UPPER.index(alphabet)
            rotation = (i + key) % len(KEY_UPPER)
            encoded += KEY_UPPER[rotation]
        else:
            encoded += alphabet

    return encoded

def rotateAscii(text, key):
    result = ""

    for character in text:
        if character.isalpha():
            if character.isupper():
                result += chr((ord(character) - 65 + key) % 26 + 65)
            else:
                result += chr((ord(character) - 97 + key) % 26 + 97)
        
        else:
            result += character

    return result

print(rotateAscii("Let's eat, Grandma!", 21))