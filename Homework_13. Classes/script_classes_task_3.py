# The move method should take a number of steps and move the robot in the direction it is currently facing. 
# The turn method should take a direction (left or right) and turn the robot in that direction.
# The display_position method should print the current position of the robot.


class Robot:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.orientation = 'up'

    def turn(self, direction):
        if direction == 'right':
            if self.orientation == 'up':
                self.orientation = 'right'
            elif self.orientation == 'right':
                self.orientation = 'down'
            elif self.orientation == 'down':
                self.orientation = 'left'
            else:
                self.orientation = 'up'
        elif direction == 'left':
            if self.orientation == 'up':
                self.orientation = 'left'
            elif self.orientation == 'left':
                self.orientation = 'down'
            elif self.orientation == 'down':
                self.orientation = 'right'
            else:
                self.orientation = 'up'        

    def move(self, steps):
        if self.orientation == 'up':
            self.position_y += steps
        elif self.orientation == 'down':
            self.position_y -= steps
        elif self.orientation == 'left':
            self.position_x -= steps
        else:
            self.position_x += steps

    def display_position(self):
        print(f'Current position is :{self.position_x},{self.position_y}, direction is {self.orientation}') 

