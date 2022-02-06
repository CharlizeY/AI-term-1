from q1 import longest_word

def test():
    word_list = ["I", "love", "Python", "programming", "the", "most"]
    output = longest_word(word_list)
    print(output)

    expected_output = ("programming", 11)

    assert output == expected_output 
    

if __name__ == "__main__":
    test()
