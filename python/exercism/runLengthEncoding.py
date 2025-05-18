def decode(string):
    decoded = ""
    i = 0

    while i < len(string):
        if string[i].isdigit():
            digit = string[i]
            while string[i + 1].isdigit():
                digit += string[i + 1]
                i += 1
            
            decoded += int(digit) * string[i + 1]
            i += 2
        else:
            decoded += string[i]
            i +=1

    return decoded


def encode(string):
    if len(string) == 1:
        return string
    curr = string[0]
    encoded = ""
    count = 0
    for character in string:
        if character == curr:
            count += 1
        else:
            encoded += curr if count == 1 else (f"{count}{curr}")
            count = 1
            curr = character
    encoded += curr if count == 1 else (f"{count}{curr}")
    return encoded


print(encode("zzz ZZ  zZ"))
print(decode("12WB12W3B24WB") == "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB")