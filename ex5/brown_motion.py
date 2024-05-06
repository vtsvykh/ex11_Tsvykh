import random


class Molecule:
    """
    Class of molecule.

    Args:
        x (int): x coordinate
        y (int): y coordinate
        radius (int): molecular radius
        color (tuple): molecular colour
        speed_x (float): speed x coordinate
        speed_y (float): speed y coordinate
    """

    def __init__(self, x, y, radius, color):
        """
        The function initialises an instance of the molecule class.

        :param x (int): x coordinate
        :param y (int): y coordinate
        :param radius (int): molecular radius
        :param color (tuple): molecular colour
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = random.uniform(1, 10)
        self.speed_y = random.uniform(1, 10)

    def move(self, window_width, window_height):
        """
        Updating the coordinates of a molecule according to its velocity.
        :param window_width: screen width
        :param window_height: screen height
        """
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < 0 or self.x > window_width:
            self.speed_x *= -1
        if self.y < 0 or self.y > window_height:
            self.speed_y *= -1
