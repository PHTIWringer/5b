# Author: Kenneth Hileman
# GitHub username: PHTIWringer
# NOTE: Will not have a ReadMe - Using another IDE
# Date: 04/26/2024
# Description: Program that tracks how far a taxicab has moved via an odometer and also how far it has moved up/down and left/right.

class Taxicab:
    def __init__(self, x_init, y_init):
        '''Creates the Taxicab class with x and y coordinates plus the odometer which tracks total movements'''
        self._x_coord = x_init
        self._y_coord = y_init
        self._odometer = 0

    def get_x_coord(self):
        '''Return the x coordinate'''
        return self._x_coord
    
    def get_y_coord(self):
        '''Return the y coordinate'''
        return self._y_coord
    
    def get_odometer(self):
        '''Return odometer reading'''
        return self._odometer
    
    def move_x(self, movement):
        '''Moves taxi on the x-axis and adds total x movements to the odometer'''
        self._x_coord += movement
        self._odometer += abs(movement)

    def move_y(self, movement):
        '''Moves taxi on the y-axis and adds total y movements to the odometer'''
        self._y_coord += movement
        self._odometer += abs(movement)
