import random

name = input("What is the name of the robot?")
# seed_number = 100
# random.seed(seed_number)
row = random.randint(0, 9)
col = random.randint(0, 9)
direction = random.choice(['North', 'South', 'East', 'West'])
id = 1000
grid_size = 10

# Correct the coordinates at the boundaries
if row < 0:
    row = 0
if col < 0:
    col = 0
if row > grid_size-1:
    row = grid_size-1
if col > grid_size-1:
    col = grid_size-1

print(f"Hello! My name is {name}. My ID is {id}.")
print(f"My current location is ({row}, {col}), facing {direction}.")

while row != 9 or col != 9:
    if direction == 'North':
        while row != 0:
            row = row - 1
            print("Moving one step forward.")
            print(f"My current location is ({row}, {col}), facing {direction}.")
        print("I have a wall in front of me!")
        print("Turning 90 degrees clockwise. ")
        direction = 'East'
        print(f"My current location is (0, {col}), facing {direction}.")

    if direction == 'South':
        while row != 9:
            row = row + 1
            print("Moving one step forward.")
            print(f"My current location is ({row}, {col}), facing {direction}.")
        if col == 9:
            break
        print("I have a wall in front of me!")
        print("Turning 90 degrees clockwise. ")
        direction = 'West'
        print(f"My current location is (9, {col}), facing {direction}.")

      
    if direction == 'East':
        while col != 9:
            col = col + 1
            print("Moving one step forward.")
            print(f"My current location is ({row}, {col}), facing {direction}.")
        print("I have a wall in front of me!")
        print("Turning 90 degrees clockwise. ")
        direction = 'South'
        print(f"My current location is ({row}, 9), facing {direction}.")
            
               
    if direction == 'West':
        while col != 0:
            col = col - 1
            print("Moving one step forward.")
            print(f"My current location is ({row}, {col}), facing {direction}.")
        print("I have a wall in front of me!")
        print("Turning 90 degrees clockwise. ")
        direction = 'North'
        print(f"My current location is ({row}, 0), facing {direction}.")

print("I am drinking Ribena! I am happy!")
