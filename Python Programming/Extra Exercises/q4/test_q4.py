from q4 import simplify_fraction

def test():
    output = simplify_fraction(4, 8)
    print(output)
    expected_output = (1, 2)
    assert output == expected_output 
    
    output = simplify_fraction(7, 9)
    print(output)
    expected_output = (7, 9)
    assert output == expected_output 
    
    output = simplify_fraction(15, 5)
    print(output)
    expected_output = (3, 1)
    assert output == expected_output 

    output = simplify_fraction(200, 300)
    print(output)
    expected_output = (2, 3)
    assert output == expected_output 

if __name__ == "__main__":
    test()
