def longest_word(word_list):
    len_list = []
    
    for word in word_list:
        len_list.append(len(word))
        max_len = max(len_list)
        max_index = len_list.index(max_len)
        longest_word = word_list[max_index]
        
    return (longest_word, max_len)


