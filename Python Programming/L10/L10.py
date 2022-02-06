### Lambda function
## Lambda in sort()
singers = [("Michael", "Jackson"), ("Billy", "Joel"), ("Lionel", "Richie"), 
           ("Tina", "Turner"), ("Luther", "Vandross")]

singers.sort(key=lambda, singer:(singer[1][-1]))

assert singers == [('Lionel', 'Richie'), 
                   ('Billy', 'Joel'), 
                   ('Michael', 'Jackson'), 
                   ('Tina', 'Turner'), 
                   ('Luther', 'Vandross')]


## Lambda in sorted()
singers = [("Michael", "Jackson"), ("Billy", "Joel"), ("Lionel", "Richie"), 
           ("Tina", "Turner"), ("Luther", "Vandross")]

sorted_singers = sorted(singers, key=lambda x:(len(x[0])+len(x[1]), x[0]))

assert sorted_singers == [('Billy', 'Joel'), 
                          ('Tina', 'Turner'),
                          ('Lionel', 'Richie'), 
                          ('Luther', 'Vandross'), 
                          ('Michael', 'Jackson')]

## Lambda in min()/max()
singers = [("Michael", "Jackson"), ("Billy", "Joel"), ("Lionel", "Richie"), 
           ("Tina", "Turner"), ("Luther", "Vandross")]

vowel_most_singer = max(singers, key=lambda x:len([char for char in x[0]+x[1] if char.lower() in 'aieou'])) 

assert vowel_most_singer == ('Lionel', 'Richie')



### Higher-order functions
## map()
fruits = ["apple", "banana", "pineapple", "pear"]

lengths = list(map(len, fruits)) # Don't forget to use list()
# lengths = [len(fruit) for fruit in fruits] # list comprehension

assert lengths == [5, 6, 9, 4]


c_temperatures = [7, 50, 12, 22, 30]

f_temperatures = list(map(lambda c: c*9/5+32, c_temperatures))
# f_temperatures = [temp*9/5 + 32 for temp in c_temperatures]

assert f_temperatures == [44.6, 122.0, 53.6, 71.6, 86.0]


## filter()
words = ["Oh", "I", "wanna", "dance", "with", "somebody"]
long_words = list(filter(lambda w:len(w) >= 5, words))
# long_words = [word for word in words if len(word) >= 5]
assert long_words == ['wanna', 'dance', 'somebody']


numbers = range(100, 300)
palindromes = list(filter(lambda n:n==int(str(n[::-1])), numbers)
# palindromes = [num for num in numbers if num==int(str(num[::-1]))]
assert palindromes == [101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292]



### More file handling
## pickle
import pickle

class Vector: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y

    def __str__(self): 
        return f"Vector ({self.x}, {self.y})"

    def __repr__(self):
        """ This makes the unique string representation
            of the object instance look more readable
        """
        return str(self)

vector1 = Vector(2, 3) 
vector2 = Vector(4, 3) 
vector = [vector1, vector2] 

# Save vector to disk. Note binary mode!
with open("vector.pkl", "wb") as file:
    pickle.dump(vector, file)

# Load pickled file that you saved earlier from disk. Again, it is a binary file!
with open("vector.pkl", "rb") as file: 
    pickled_vectors = pickle.load(file)

print(pickled_vectors)  ## [Vector (2, 3), Vector (4, 3)]

print(type(pickled_vectors))  ## <class 'list'>


## csv
# Read csv
import csv

with open("grades.csv") as csv_file: 
    reader = csv.reader(csv_file, delimiter=",", skipinitialspace=True) 
    header_row = next(reader) 

    for row in reader:
        first_name = row[1]
        last_name = row[0]
        final_marks = row[7]
        grade = row[8]
            
        print(f"{first_name} {last_name}: {final_marks} ({grade})")

# Alternatively
with open("grades.csv") as csv_file: 
    reader = csv.DictReader(csv_file, skipinitialspace=True)

    for row in reader:
        first_name = row["First name"]
        last_name = row["Last name"]
        final_marks = row["Final"]
        grade = row["Grade"]
            
        print(f"{first_name} {last_name}: {final_marks} ({grade})")

# Write csv
with open("grades.csv") as csv_file:
    headers = ["First name", "Last name", "Final", "Grade"]
    data = []
    
    reader = csv.reader(csv_file, delimiter=",", skipinitialspace=True)

    for row in reader:
        data = data.append([row[header] for header in headers])
        
with open("final.csv", "w") as csv_file: 
    writer = csv.writer(csv_file) 
    writer.writerow(headers)
    writer.writerows(data)

# Alternatively
with open("grades.csv") as csv_file:
    headers = ["First name", "Last name", "Final", "Grade"]
    data = []
    
    reader = csv.reader(csv_file, delimiter=",", skipinitialspace=True)

    for row in reader:
        data = data.append({header: row[header] for header in headers})
        
with open("output_students.csv", "w") as csv_file: 
    writer = csv.DictWriter(csv_file, fieldnames=headers, delimiter="|") 
    writer.writeheader() 
    writer.writerows(data)
