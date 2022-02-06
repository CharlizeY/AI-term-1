## Refactor the prime number validator
def is_divisible_by(number, divisor):
    return number % divisor == 0 # True or False


def is_prime_number(number):
    if number <= 1:
        return(False)

    divisor = 2
    
    while divisor < number:
        if is_divisible_by(number, divisor):
            return(False) # The function stops at any return value
        else:
            divisor += 1
            
    return(True)


def read_integer():
    entry = int(input("Please enter an integer: "))
    return(entry)


n = read_integer()

if is_prime_number(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")



## Refactor the prime number generator
def generate_prime_numbers(maximum):
    n = 2
    while n <= maximum:
        if is_prime_number(n):
            print(n)
        n += 1

        
last_number = read_integer()
generate_prime_numbers(last_number)



## Test and implement manhattan_distance() function
def manhattan_distance(x1, y1, x2, y2):
    """ Calculate the Manhattan distance between two points (x1, y1) and (x2, y2).
    Args:
        x1 (float) : the x coordinate of the first point
        y1 (float) : the y coordinate of the first point
        x2 (float) : the x coordinate of the second point
        y2 (float) : the y coordinate of the second point

    Returns:
        float : the Manhatten distance between two specified points
    """
    hori_dist = abs(x1-x2)
    vert_dist = abs(y1-y2)
    manhatten_dist = hori_dist + vert_dist
    return(manhatten_dist)

    
def test_manhattan_distance():
    """ Test if the manhattan_distance() function calculates the Manhanttan distance correctly
        between two points (2, -2) and (3, 1).
    """
    distance = manhattan_distance(2, 3, -2, 1)
    expected_answer = 6
    epsilon = 0.000001
    assert abs(distance - expected_answer) < epsilon f"Test failed. {expected_answer} expected, but {distance} returned."


test_manhattan_distance()
