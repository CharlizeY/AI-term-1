## Create a function that adds an integer to each element in the list of integers
# A simple solution using 'for' loop
def increment_list(list_of_int, step=1):
    """ Increment each integer in a list by the given step.

    Args:
        list_of_int(list): A list of integers.
        step(int): The incremental step for each integer in the list. Defaults to 1.

    Returns:
        A list of incremented integers by the given step.
    """
    return [x+step for x in list_of_int] # Returns a list


# A more fundamental solution using the while loop and increment argument
def increment_list(list_of_int, step=1):
    new_list = []
    
    while index < len(list_of_int):
        new_element = list[index] + step
        new_list = new_list.append(new_element)
        index += 1
        
    return(new_list)



## Define functions that returns the smallest number in a list of integers
def compute_min(numbers): # Input is a list of numbers
    if len(numbers) == 0:
        print("No number is in the list.")
        return None

    smallest_number = numbers[0]
    for number in numbers:
        if number < smallest_number:
            smallest_number = number
    return(smallest_number)


def read_input_from_user():
    integer = input("Please enter an integer:")
    numbers = [integer]
    while integer != "q":
        integer = int(input("Read an integer:"))
        numbers.append(integer)
    return(numbers)


def run_program():
    numbers = read_input_from_user()
    print(compute_min(numbers))

run_program()



## Define a function that returns the smallest number in a list of integers that is divisible by the given divisor
def compute_min_divisable(numbers, divisor):
    divisible_list = []
    
    for number in numbers:
        if number % divisor == 0:
            divisible_list.append(number)
            
    print(len(divisible_list))
    
    if len(divisible_list) == 0:
        return None
    else:
        min_divisible_number = min(divisible_list)
        # min_divisible_number = compute_min(divisible_list)
        return(min_divisible_number)


# Testing
def test_example():
    result = compute_min_divisible([66, 33, -55, 11], 11)
    expected_result = -55
    assert result == expected_result


def test_none_divisible():
    result = compute_min_divisible([34, 5, 10, 19, 28, 74], 3)
    expected_result = None
    assert result == expected_result


def test_single():
    result = compute_min_divisible([25], 5)
    expected_result = 25
    assert result == expected_result


def test_single_nondivisible():
    result = compute_min_divisible([8], 7)
    expected_result = None
    assert result == expected_result

test_example()
test_none_divisible()
test_single()
test_single_nondivisible()



## Define a function that returns a nested list with specified length
## where each element is a list containing the integers from 1 to the current number
def generate_triangle_list(length):
    list = []
    
    for number in range(1,length+1):
        new_list = list(range(1,number))
        print(new_list)
        list = list.append(new_list)
        
    return(list)


# Testing
def test_example():
    result = generate_triangle_list(3)
    expected_result = [[1], [1, 2], [1, 2, 3]]
    assert result == expected_result


def test_one():
    result = generate_triangle_list(1)
    expected_result = [[1]]
    assert result == expected_result


def test_zero():
    result = generate_triangle_list(0)
    expected_result = []
    assert result == expected_result

test_example()
test_one()
test_zero()



## Define a function that returns a list of cumulative sums of a list of integers
def compute_cumulative_sum(list_of_integers):
    length = len(list_of_integers)
    list_of_cumsum = [None] * length # Initiate an empty list with certain size
    
    for index in range(length):
        list_of_cumsum[index] = sum(list_of_integers[0:(index+1)])
        
    return(list_of_cumsum)


# Testing
def test_example():
    result = compute_cumulative_sum([3, 5, 4, 1, 2])
    expected_result = [3, 8, 12, 13, 15]
    assert result == expected_result

    
def test_single():
    result = compute_cumulative_sum([6])
    expected_result = [6]
    assert result == expected_result

    
def test_empty():
    result = compute_cumulative_sum([])
    expected_result = []
    assert result == expected_result

test_example()
test_single()
test_empty()



## Define a function that returns a list of the Fibonacci sequence up until the given length
def generate_fibonacci(length):
    if length == 0:
        list_of_fibonacci = []
        return(list_of_fibonacci)
    
    else:
        list_of_fibonacci = [None] * length
        list_of_fibonacci[0] = 0
        list_of_fibonacci[1] = 1
        for index in range(2,length):
            list_of_fibonacci[index] = sum(list_of_fibonacci[(index-2):index])
            
        return(list_of_fibonacci)


# Testing
def test_example():
    result = generate_fibonacci(10)
    expected_result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert result == expected_result


def test_one():
    result = generate_fibonacci(1)
    expected_result = [0]
    assert result == expected_result

    
def test_zero():
    result = generate_fibonacci(0)
    expected_result = []
    assert result == expected_result



## Define a function that appends a list of suffixes to the end of each string in another list
def add_suffixes(words, suffixes):
    nested_list = []
    for suffix in suffixes:
        single_list = []
        for word in words:
            complete_word = word + suffix
            single_list.append(complete_word)
        nested_list.append(single_list)
        
    return(nested_list)


# Testing
def test_function():
    words = ["consult", "print", "walk"]
    suffixes = ["ed", "ing"]
    result = add_suffixes(words, suffixes)
    expected_result = [["consulted", "printed", "walked"],
        ["consulting", "printing", "walking"]]
    print(result)
    assert result == expected_result
    

def load_verbs_from_file(filename):
    verbs = []
    textfile = open(filename)
    for line in textfile:
        verb = line.strip()  # strips off the "\n" at the end of each line
        verbs.append(verb)
    return verbs

verbs = load_verbs_from_file("verbs1.txt")


def run_program():
    verbs = load_verbs_from_file("verbs1.txt")
    suffixes = ["ing", "ed"]
    suffixed_verbs_list = add_suffixes(verbs, suffixes)
    for suffixed_verbs in suffixed_verbs_list:
        for verb in suffixed_verbs:
            print(verb)

test_function()
run_program()



## Define a function that checks whether a given string is a palindrome
def is_palindrome(string):
    return(string[::-1] == string)
    
is_palindrome("kayak")
is_palindrome("python")



## Define a function that replaces all occurrences of the first character of a string with "_"
def blankify(string):
    new_string = ""
    for letter in string:
        if letter == string[0]:
            new_string += "_"
        else:
            new_string += letter
    return(new_string)

blankify("easy peasy lemon squeezy")
blankify(" amazing grace how sweet the sound")
blankify("")
