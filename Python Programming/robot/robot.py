class Robot:
    def __init__(self, identifier, name, position, direction):
        self.id = identifier
        self.name = name
        self.position = position
        self.direction = direction


    # Print robot messages
    def greet(self):
        print(f"Hello. My name is {self.name}. My ID is {self.id}.")


    def search_drink_message(self):
        print(f"{self.name} is searching for its drink.")
   
    
    def current_location(self):
        print(f"My current location is {self.position}, facing {self.direction}.")


    def step_forward_message(self):
        print("Moving one step forward.")


    def hit_a_wall_message(self):
        print("I have a wall in front of me!")


    def turn_clockwise_message(self):
        print("Turning 90 degrees clockwise. ")


    def get_ribena_message(self):
        print("I am drinking Ribena! I am happy!")



    # Navigate the robot to ribena
    def step_forward(self):
        """ Make robot move one step forward in the current direction.
        """
        (row,col) = self.position
        
        if self.direction == 'North':
                row -= 1
        if self.direction == 'South':
                row += 1
        if self.direction == 'East':
                col += 1        
        if self.direction == 'West':
                col -= 1
        self.position = (row,col)


    def hit_a_wall(self):
        """ Check whether the robot hits a wall or not (True/False).
        """
        (row,col) = self.position
        
        return(self.direction == "North" and row == 0
                   or self.direction == "South" and row == 9
                   or self.direction == "East" and col == 9
                   or self.direction == "West" and col == 0) 


    def move_to_the_wall(self):
        """ Move the robot in the direction specified until it hits the wall.
        """
        while not self.hit_a_wall():
            self.step_forward()
            self.step_forward_message()
            self.current_location()


    def turn_clockwise(self):
        """ Turn the robot clockwise for 90 degrees.
        """    
        if self.direction == "North":
            self.direction = "East"
        elif self.direction == "South":
            self.direction = "West"   
        elif self.direction == "East":
            self.direction = "South"
        elif self.direction == "West":
            self.direction = "North"
        else:
            print(f"Error rotating 90 degrees clockwise. Unknown direction {self.direction}.")
            exit()


    def reach_target_location(self, target_position):
        """ Check whether the robot reaches the target coordinates or not (True/False).
        """
        return(self.position == target_position)


    def navigate(self, target_position, grid_size):
        """ Have robot automatically navigate to a target grid cell.
        """
        while not self.reach_target_location(target_position):
            self.move_to_the_wall()
            if self.reach_target_location(target_position):
                break
            self.hit_a_wall_message()
            self.turn_clockwise()
            self.current_location()
        self.get_ribena_message()
