from q2 import filter_e

def test():
    output = filter_e("I swear by the moon and the stars in the sky")
    print(output)

    expected_output = "I by moon and stars in sky"

    assert output == expected_output 
    

if __name__ == "__main__":
    test()
