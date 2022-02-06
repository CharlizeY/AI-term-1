from q3 import convert

def test():
    output = convert(38)
    print(output)
    expected_output = (0, 0, 38)
    assert output == expected_output 
    
    output = convert(176)
    print(output)
    expected_output = (0, 2, 56)
    assert output == expected_output 

    output = convert(3823)
    print(output)
    expected_output = (1, 3, 43)
    assert output == expected_output 

if __name__ == "__main__":
    test()
