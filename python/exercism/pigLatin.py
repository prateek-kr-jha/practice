def translate(text):
    end_suffix = "ay"

    if text.lower().startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt', 'ay')):
        print("found vowel")
        return text + end_suffix
    
    if not text.startswith("qu"):
        for i,char in enumerate(text):
            if char.lower() in "aeiou":
                return text[i:] + text[:i] + end_suffix   
 
    if "qu" in text:
        print(4)
        index = text.index("qu") + 2
        return text[index:] + text[:index] + end_suffix
    
    if "y" in text:
        print(2)
        index = text.index("y") + 1

    return text + end_suffix

word = "square" # are squ ay
print(translate(word))
# id
# Rules:
# 1. vowels or "xr" or "yt" or an "end_suffix" = word + "end_suffix"
# 2. one or more consonants e.g. (xyz) + remaining word = remaining word + (xyz) + "end_suffix"
# 3. one or more consonants e.g. (xyz) + "y" + remaining word = "y" + remaining word + (xyz) + "end_suffix" 
# 4. zero or more consonants + "qu" + remaining word = remaining word + consonant + "qu" + "end_suffix"
print(not word.startswith("qu"))