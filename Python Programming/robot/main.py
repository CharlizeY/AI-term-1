import random
from robot_init import RobotFactory


def read_robot_names(filepath):
    names = []
    with open(filepath) as file:
        for line in file:
            name = line.strip()
            names.append(name)
        return names


def run_simulation(filepath, count, grid_size=10, target_position=(9,9)):
    """ Start a simulation session of a robot navigating to a target grid cell.

    Args:
        grid_size (int): The size of the grid. Defaults to 10.
        target_position (tuple): The target coordinates. Defaults to (9,9).
    """
    robot_names = read_robot_names(filepath)
    robot_factory = RobotFactory(robot_names, grid_size=10)
    robots = robot_factory.create_robots(count)
    for robot in robots:
        robot.greet()
        robot.search_drink_message()
        robot.current_location()
        robot.navigate(target_position, grid_size)
        print()
    

# Ribena must be at the corner of the map, i.e. target_position should be one of {(0,0),(0,9),(9,0),(9,9)}
ribeha_position = random.choice([(0,0), (0,9), (9,0), (9,9)])
run_simulation(filepath="robot_names.txt", count=3, grid_size=10, target_position=ribeha_position)



