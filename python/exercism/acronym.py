def abbreviate(words):
    words_list = words.replace("-", " ").replace("_", "").split(" ")
    print(words_list)
    acronym = ""
    for word in words_list:
        print(word)
        if len(word) and word[0].isalnum():
            acronym += word[0].upper()

    return acronym


print(abbreviate("First In, First Out"))