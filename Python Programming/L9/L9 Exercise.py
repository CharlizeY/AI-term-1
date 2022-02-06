## OOP Exercises
class Car:
    def __init__(self, model, year, is_manual, max_passengers=5, wheels):
        self.model = model
        self.year = year
        self.is_manual = is_manual
        self.max_passengers = max_passengers
        self.speed = 0
        self.rotation = 0
        self.wheels = wheels

# Define class methods
    def compute_true_rate(self, rate):
        true_rate = rate
        for wheel in self.wheels:
            true_rate -= 0.5*wheel.resistance
        return max(0, true_rate)
    
    def accelerate(self, rate=1):
        true_rate = compute_true_rate(rate)
        self.speed += true_rate

    def decelerate(self, rate=1)
        true_rate = compute_true_rate(rate)
        new_speed = self.speed - true_rate
        self.speed = max(0, new_speed)

    def brake(self):
        self.speed = 0

    def steer(self, angle):
        new_angle = self.rotation + angle
        self.rotation = max(min(new_angle, 180), -180)          



class Driver:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def drive(self, car):
        print(f"Driver {self.name} is driving a {car.model}")
        print(f"Driver {self.name} is accelerating the car.")
        car.accelerate(20)
        print(f"The car's speed is now {car.speed}.")
        print(f"Driver {self.name} is steering the car.")
        car.steer(90)
        print(f"The car's rotation is now {car.angle}.")
        print(f"Driver {self.name} is braking the car.")
        car.brake()
        print(f"The car's speed is now {car.speed}.")
        print(f"Driver {self.name} has finished driving.")



class Wheel:
    def __init__(self, resistance, diameter):
        self.resistance = resistance
        self.diameter = diameter



class BattleCar(Car):
    def __init__(self, model, year, is_manual, wheels, max_passengers=5, strength=0):
        super().__init__(model, year, is_manual, wheels, max_passengers)
        self.strength = strength
        
    def attack(self, car):
        car.decelerate(self.strength)


class BoosterCar(Car):
    def __init__(self, model, year, is_manual, wheels, max_passengers=5, boost=1):
        super().__init__(model, year, is_manual, wheels, max_passengers)
        self.boost = boost
        
    def accelerate(self, rate):
        super().accelerate(rate * self.boost)



# Testing
def run_simulation():      
    sports_car = Car("Porsche GT2", 2006, True, 4)
    driver = Driver("F123", "Michael Schumacher")
    driver.drive(sports_car)

    
def test_decelerate():
    # create 4 wheels
    diameter = 36
    resistance = 0.5
    num_of_wheels = 4
    wheels = []
    for i in range(num_of_wheels):
        wheels.append(Wheel(diameter, resistance))
        
    car = Car("Honda Civic", 2015, False, wheels)
    
    car.accelerate(10)
    assert car.speed == 9
    
    car.decelerate(4) 
    assert car.speed == 6


def test_battlecar():
    diameter = 38
    resistance = 0.5
    num_of_wheels = 4
    wheels = []
    for i in range(num_of_wheels):
        wheels.append(Wheel(diameter, resistance))
 
    battle_car_strength = 5
    battle_car = BattleCar("The Terminator", 2020, True, wheels,
                           strength=battle_car_strength)
    
    opponent_car = Car("Honda Civic", 2015, True, wheels)
    print("Opponent car accelerates...", end="")
    opponent_car.accelerate(50)
    print(f"speed is now {opponent_car.speed}")
    assert opponent_car.speed == 49

    print("Battle car accelerates...", end="")
    battle_car.accelerate(40)
    print(f"speed is now {battle_car.speed}")
    assert battle_car.speed == 39
    
    print("Battle car attacks opponent car.")
    battle_car.attack(opponent_car)
    print(f"Opponent car's speed is now {opponent_car.speed}")
    assert opponent_car.speed == 45


def test_boostercar():
    diameter = 38
    resistance = 0.5
    num_of_wheels = 4
    wheels = []
    for i in range(num_of_wheels):
        wheels.append(Wheel(diameter, resistance))
 
    boost = 1.2
    booster_car = BoosterCar("Super Sonic", 2021, True, wheels,
                           boost=boost)
    
    print("Booster car accelerates...", end="")
    booster_car.accelerate(20)
    print(f"speed is now {booster_car.speed}")
    assert booster_car.speed == 23
     
    print("Booster car accelerates...", end="")
    booster_car.accelerate(10)
    print(f"speed is now {booster_car.speed}")
    assert booster_car.speed == 34
    
    print("Booster car decelerates...", end="")
    booster_car.decelerate(10)
    print(f"speed is now {booster_car.speed}")
    assert booster_car.speed == 34-9
    

if __name__ == "__main__":
    run_simulation()
    test_decelerate()
        


## More Iterable Objects Exercises
# enumerate
def get_word_positions(list_of_str):
    positions = {}
    for position, word in enumerate(list_of_str):
        positions.setdefault(word, []).append(position)
        
    return(positions)


# zip
def concatenate_feature_labels(x,y):
    concatenated_list = []
    for (features, output) in zip(x, y):
        concatenated_list.append(features.append(output))
        
    return concatenated_list

# Testing for zip
def test_concat():
    x = [[0.2, 0.3], 
         [0.5, 0.4], 
         [0.1, 0.2], 
         [0.2, 0.2], 
         [0.4, 0.5], 
         [0.5, 0.5]]
    y = [1, 2, 1, 1, 2, 2]
    
    dataset = concatenate_feature_labels(x, y)
    print(dataset)
    
    expected = [
        [0.2, 0.3, 1], 
        [0.5, 0.4, 2], 
        [0.1, 0.2, 1], 
        [0.2, 0.2, 1], 
        [0.4, 0.5, 2], 
        [0.5, 0.5, 2]
    ]
    
    assert dataset == expected



## List Comprehension Exercises
numbers = [i*i for i in range(50) if i%2 == 0 and i%3 == 0]
print(numbers)


numbers = [[1, 2], [2, 3, 4], [4, 5]]
new_numbers = [value for number_list in numbers for value in number_list]
assert new_numbers == [1, 2, 2, 3, 4, 4, 5]


ids = {"Luca": "20013", "Josiah": "10027", "Rob": "10112", "Harry": "20064"}
names = {value: key for (key, value) in ids.items() if value[0] == "2"}
assert names == {'20013': 'Luca', '20064': 'Harry'}


    
## JSON files Exercises
import json
import sys

# Open the JSON file
def load_json(filename):
    with open(filename, "r") as jsonfile: 
        data = json.load(jsonfile)
    return data


# Write to the JSON file
def save_json(data, filename):
with open(filename, "w") as jsonfile: 
    json.dump(data, jsonfile)


# Convert the loaded data into a list
def convert_format(data):
    annotations = data["annotations"]
    images = data["images"] 
    for annotation in annotations:
        del annotation["image_id"]
        for image in images:
            image.update({"annotations": annotation})
    return images


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please give the input and output filename of the JSON files")
        print("Example: python chap06_5_sys.py input.json output.json")
        exit()


data = load_json(sys.argv[1])
reformatted_data = convert_format(data)
save_json(reformatted_data, sys.argv[2])








    
