# def decode(string):
#     decoded = ""
#     i = 0

#     while i < len(string):
#         if string[i].isdigit():
#             digit = string[i]
#             while string[i + 1].isdigit():
#                 digit += string[i + 1]
#                 i += 1
            
#             decoded += int(digit) * string[i + 1]
#             i += 2
#         else:
#             decoded += string[i]
#             i +=1

#     return decoded


# def encode(string):
#     if len(string) == 1:
#         return string
#     curr = string[0]
#     encoded = ""
#     count = 0
#     for character in string:
#         if character == curr:
#             count += 1
#         else:
#             encoded += curr if count == 1 else (f"{count}{curr}")
#             count = 1
#             curr = character
#     encoded += curr if count == 1 else (f"{count}{curr}")
#     return encoded


from typing import Iterator
import re

def _group_chars(text: str) -> Iterator[tuple[str, str]]:
    """Group consecutive characters with their counts."""
    matches = re.finditer(r'(\d+)?([A-Za-z\s])', text)

    for match in matches:
        # print(match.groups(), "-----------------------")
        count, char = match.groups()
        yield int(count) if count else 1, char

def decode(text: str) -> str:
    """
    Decode run-length encoded string.
    
    Args:
        text: Encoded string like "2A3B" representing "AABBB"
        
    Returns:
        Decoded string

    """
    # print(count, char for count, char in _group_chars(text))
    return ''.join(char * count for count, char in _group_chars(text))

def encode(text: str) -> str:
    """
    Encode string using run-length encoding.
    
    Args:
        text: String to encode
        
    Returns:
        Encoded string where repeated chars are replaced with count + char
    """
    if not text:
        return ''
        
    result = []
    count = 1
    prev_char = text[0]
    
    for char in text[1:]:
        if char == prev_char:
            count += 1
        else:
            result.append(f"{count if count > 1 else ''}{prev_char}")
            count = 1
            prev_char = char
            
    result.append(f"{count if count > 1 else ''}{prev_char}")
    return ''.join(result)




# print(encode("zzz ZZ  zZ"))
# print(decode("12WB12W3B24WB") == "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB")

def test():
    count = 10
    return int(count) if count else 1, "X"

print(test())