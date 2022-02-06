import pprint

## Define a function that checks whether a given sentence is a palindrome
def modify_sentence(sentence):
    """ Modify a sentence so that it only contains lower-case characters and spaces.
    """
    clean_sentence = [] # list of characters
    for char in sentence:
        if char.isalpha():
            clean_sentence.append(char)
            
    return "".join(clean_sentence).lower


def is_palindrome(sentence):
    """ Check whether a given sentence is a palindrome.
    """
    clean_sentence = modify_sentence(sentence)
    return clean_sentence == clean_sentence[::-1] # reverse a string

    
is_palindrome("Step on no pets!")
is_palindrome("Eva, can I see bees in a cave?")
is_palindrome("Hello, my friend!")



## Define a function that replaces each letter with a letter N steps further down the alphabet
import string

lower_case_alphabet = string.ascii_lowercase
upper_case_alphabet = string.ascii_uppercase

def apply_cipher(string, N=0):
    new_str = [] # list of characters
    
    for char in string:
        if char.islower():
            new_index = (lower_case_alphabet.find(char) + N) % 26
            new_char = lower_case_alphabet[new_index]
        elif char.isupper():
            new_index = (upper_case_alphabet.find(char) + N) % 26
            new_char = upper_case_alphabet[new_index]
        else:
            new_char = char
            
        new_str.append(new_char)
        
    return "".join(new_str) # return a string



apply_cipher("Python Programming", 10)
apply_cipher("THE quick Brown fox JuMpS Over the lazy dog", -3)
apply_cipher("THE quick Brown fox JuMpS Over the lazy dog") # No movement



## Define a function that checks whether the parentheses in an expression are balanced
def is_parenthesis_balanced(str_of_paren):
    stack = []
    for paren in str_of_paren:
        if paren == "(":
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop(-1) # Remove the latest "(" added to the stack
                
    if len(stack) == 0:
        return True
    else:
        return False


is_parenthesis_balanced("(()(()))")
is_parenthesis_balanced("())")
is_parenthesis_balanced(")(()")
is_parenthesis_balanced("")



## Define a function that compute the factorial of a positive integer
# Using loops
def factorial(n):
    product = 1
    while n >= 1:
        product *= n
        n -= 1
    return(product)


# Using recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)



## Define a recursive function that returns the fibonacci number at a given position
def fibonacci(position):
    if position == [0, 1]: # one of them in the list
        return position
    else:
       return fibonacci(position-2) + fibonacci(position-1)


# Testing
def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55


test_fibonacci()



## Exercises for dictionaries
# Read a text file and return a dictionary of employee IDs (key) and names (value)
def load_database(filename):
    dict = {}
    textfile = open(filename)
    for line in textfile:
        (id, name) = line.strip().split(",")
        dict[id] = name
    return(dict)

  
employee_dict = load_database("employees.txt")
print(employee_dict)



# Given the employee IDs, retrive their names from the dictionary
def query_employees(dict,query_list):
    retrived_names = []
    for query in query_list:
        name = dict.get(query, None) # returns None if the key doesn't exist
        retrived_names.append(name)
    return retrived_names


employee_dict = load_database("employees.txt")
queries = ["14817102", "12345678", "61098940"]
names = query_employees(employee_dict, queries)
print(names)



# Read a textfile and return a list of dict representations of the employees
# each dict contains the employee’s id, name, age and nationality as keys
def load_employees(filename):
    
    employees = []
    
    with open(filename) as textfile:
        for line in textfile:
            (id, name, age, nationality) = line.strip().split(",")
            age = int(age)
            employees.append({"id": id, "name": name, "age": age, "nationality": nationality})
    return employees

          
employees = load_employees("employees_detail.txt")
print(len(employees))
print(employees[0])
# pprint.pp(employees[0])



# Filter the employees (lists) with specific attribute values
def filter_employees(employees, filter_criterion):
    
    filtered_employees = []
    
    (attribute, value) = filter_criterion
    for employee in list_of_employees:
        if employee[attribute] = value:
            filtered_employees.append(employee)
            
    return filtered_employees


def test_pipeline():
    employees = load_employees("employees_detail.txt")
    result = filter_employees(employees, ("nationality", "japan"))
    expected = [
        {'id': '06106396', 'name': 'Monika Moray', 'age': 37, 
         'nationality': 'japan'}, 
        {'id': '87491761', 'name': 'Bernarda Alexander', 'age': 43,
         'nationality': 'japan'}, 
        {'id': '14817102', 'name': 'Agathe Davies', 'age': 39, 
         'nationality': 'japan'}
    ]
    assert result == expected


# Read a textfile and return a dict of dict representations of the employees
# each dict contains the employee’s id, name, age and nationality as keys
def load_indexed_employees(filename):
    
    employees_dict = {}
    
    with open(filename) as textfile:
        for line in textfile:
            (id, name, age, nationality) = line.strip().split(",")
            age = int(age)
            employees_dict[id] = {"id": id, "name": name, "age": age, "nationality": nationality}
    return employees_dict

          
employees_dict = load_indexed_employees("employees_detail.txt")
print(len(employees))
employee_ids = list(employee_dict) # a list of keys, same as employee_dict.keys()
print(employee_ids)
print(employee_dict[employee_ids[0]])
# pprint.pp(employees[0])



# Return a dict where the keys are English words, and the values are a list of possible French translations
def load_translations(filename):
    dict_of_translations = {}
    
    with open(filename) as textfile:
        all_lines = textfile.readlines() # Read the whole textfile, suitable for small files

    for line in all_lines:
        list_of_words = list(line.strip().split())
        english = list_of_words[0]
        french = list_of_words[1:]
        dict_of_translations[english] = french
        
    return dict_of_translations


translation_dict = load_translations("french.txt")



# Return the translation of the given english sentence based on the given translation dictionary.
def translate(english_sentence, dict_of_translations):
    list_of_translations = []
    
    seperated_words = english_sentence.split()
    for word in seperated_words:
        if word in dict_of_translations.keys():
            translation = dict_of_translations[word][0] # choose the first French translation
            list_of_translations.append(translation)
            
    return " ".join(list_of_translations) # with empty space between words


def test_pipeline():
    translation_dict = load_translations("french.txt")
    result = translate("a boy with a ball in the park", translation_dict)
    print(result)
    expected = "un garçon avec un balle dans le parc"
    assert result == expected



## Exception Handling Exercises
# List of fruits
fruits = ["apples", "oranges", "bananas", "pineapples", "mangoes"]

try:
    index = int(input("Enter an integer: "))
except ValueError:
    print("Please enter an integer index.")
    
try:
    fruit = fruits[index]
except IndexError:
    print("Please enter an integer between -5 and 4.")
else:
    print(f"You love {fruit}!")


# Opening a file
try:
    with open("nosuchfile.txt") as textfile:
        for line in textfile:
            print(line)
except NofileError:
    print("There is no such file named nosuchfile.txt in your directory.")
finally:
    print("I have an important message!")



        
