## Sets
# Define a function that returns a set of words that are common in both files
def get_vocabulary(filename):
    
    vocabularies = set()
    
    with open(filename) as textfile:
        for line in textfile:
            vocabularies.update(set(line.strip().split(" "))
                                
    return(vocabularies)   

            
def get_overlapping_words(filename1, filename2):
    words_of_file1 = get_vocabulary(filename1)
    words_of_file2 = get_vocabulary(filename2)
    overlap_words = words_of_file1.intersection(words_of_file2)
    
    return(overlap_words)


overlap = get_overlapping_words("let_it_go.txt", "into_the_unknown.txt")
print(overlap)
print(len(overlap))



## Classes Exercise
class Car:
    def __init__(self, model, year, is_manual, max_passengers=5):
        self.model = model
        self.year = year
        self.is_manual = is_manual
        self.max_passengers = max_passengers
        self.speed = 0
        self.rotation = 0


# Define class methods
    def accelerate(self, rate=1):
        self.speed += rate

    def decelerate(self, rate=1)
        new_speed = self.speed - rate
        self.speed = min(0, new_speed)

    def brake(self):
        self.speed = 0

    def steer(self, angle):
        new_angle = self.rotation + angle
        self.rotation = max(-180, min(new_angle, 180))
            

def test_default_passengers():
    model = "Honda Civic"
    year = 2015
    is_manual = False
    
    my_car = Car(model, year, is_manual)
    
    assert isinstance(my_car, Car)

    assert my_car.model == model
    assert my_car.year == year
    assert my_car.is_manual == is_manual
    assert my_car.max_passengers == 5
    assert my_car.speed == 0
    assert my_car.rotation == 0



# Use the __str__ method to return a more readable string representation of the object
# Use the __lt__ method to overwrite '<' (magical method)
class Person:
    def __init__(self, name, age, nationality="uk"):
        self.name = name
        self.age = age
        self.nationality = nationality

    def __str__(self):
        return f"A Person named {self.name} aged {self.age} from {self.nationality}."

    def __lt__(self, other):
        """ Compare two instances of Person by their age.

        Args:
            other (Person) : the other Person instance against to compare

        Returns:
            bool : True if the person's age is smaller than the other person's age. False otherwise.
        """
        
        return self.age < other.age
    

lecturer = Person("Josiah", 20, "malaysia")
print(lecturer)

assistant1 = Person("Harry", 11, "uk")
assistant2 = Person("Joe", 18, "uk")
print(assistant1 < assistant2)  # should print True, uses the magical method __lt__
print(assistant2 < assistant1)  # should print False



## Read and write files
def convert_to_lowercase(filename):
    outfilename = filename.replace(".txt", "_lower.txt")
    
    with open(filename, "r") as infile, open(outfilename, "w") as outfile:
        for line in infile:
            words = line.lower().strip().split()
            for word in words:
                outfile.write(f"{word}\n") # Convert list element to string

    return outfilename



## Input Validation
# LBYL
def find_in_list(numbers, query):
    if query not in numbers:
        print("The query n was not found in numbers. Returning 0.")
        return 0
    
    position = numbers.index(query)

    if position != len(numbers)-1:
        return numbers[position] + numbers[position+1]
    else:
        return query


# EAFP
def find_in_list(numbers, query):
    try:
        position = numbers.index(query)
    except ValueError:
        print(f"{query} was not found in {numbers}. Returning 0.")
        return 0
    
    try:
        numbers[position] + numbers[position+1]
    except IndexError:
        return numbers[position]


    








