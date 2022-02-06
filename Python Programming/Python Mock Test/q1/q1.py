def odd_even_swap(word):
    split_word = list(word)
    for i in range(1, len(split_word)):
        if (i % 2) != 0:
            split_word[i-1], split_word[i] = split_word[i], split_word[i-1]
    word = "".join(split_word)
    return(word)
