def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	



words = input("Please enter some words space separated words: ")
length = int(input("Please enter a length for words: "))


print(long_words(length, words))