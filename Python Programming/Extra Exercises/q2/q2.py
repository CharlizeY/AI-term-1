def filter_e(string):
    new_string_list = []
    words = string.split(' ')
    
    for word in words:
        if 'e' not in word:
            new_string_list.append(word)
    new_string = " ".join(new_string_list)
    
    return new_string

