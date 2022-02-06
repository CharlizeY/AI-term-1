import random
from robot import Robot


class RobotFactory:
    def __init__(self, robot_names, grid_size=10): 
        self.names = robot_names
        self.grid_size = grid_size

    
    def create_robots(self, count=1):
        robots = []
        for i in range(count):
            robots.append(self.create_robot())
        return robots


    def create_robot(self):
        """ Initialise the robot name, ID, and initial position and direction.
        """
        name = self._generate_name("robot_names.txt")
        id = self._generate_id()
        position = self._generate_location()
        direction = self._generate_direction()
        robot = Robot(id, name, position, direction)

        return robot
    

    def _generate_name(self, filename):
        """ Randomly choose the name of the robot from a list of pre-defined names in a file.
        """
        return random.choice(self.names) # Randomly choose one name in the list


    def _generate_id(self):
        """ Generate the pre-defined robot ID.
        """
        self.robot_id = random.randint(0,10000)


    def _generate_location(self):
        """ Randomly generate the initial location of the robot within the grid.

        Args:
            grid_size (int): The size of the grid. Defaults to 10。

        Returns:
            int : Robot's row coordinate
            int : Robot's column coordinate
            str : Robot's direction ("North", "South", "East", or "West")
        """
        row = random.randint(0, self.grid_size-1)
        col = random.randint(0, self.grid_size-1)
        position = (row, col)
        
        return(position)


    def _generate_direction(self):
        """ Randomly generate the initial direction that the robot is facing.
        """
        direction = random.choice(['North', 'South', 'East', 'West'])
        
        return(direction)

     
    def _clip_position_to_boundary(self, position):
        """ Correct the position of robot if it is outside the boundaries.
        """
        (row, col) = position
        
        if row < 0:
            row = 0
        if col < 0:
            col = 0
        if row > self.grid_size-1:
            row = self.grid_size-1
        if col > self.grid_size-1:
            col = self.grid_size-1
            
        return (row, col)
    
