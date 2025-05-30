import string as string
import random

def find_anagrams(word, candidates):
    return [
        candidate
        for candidate in candidates
        if candidate.lower() != word.lower()
        and sorted(candidate.lower()) == sorted(word.lower())
    ]

candidates = ["lemons", "cherry", "melons"]
print(find_anagrams("solemn", candidates))
