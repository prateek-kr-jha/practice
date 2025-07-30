wordlist = ['cat','dog','rabbit']
letterlist = [char for animal in wordlist for char in animal]
print(letterlist)
print(list(set(letterlist)))
