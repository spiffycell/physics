""" Classes and methods associated with Analysis."""
# imports
from pydantic import BaseModel
from typing import List
import math
import numpy as np

# classes
class Vector(BaseModel):
    """ 
    @desc   Vector object.
    @param  BaseModel from pydantic
    @see
    """
    x: float
    y: float
    z: float

    def __init__(self):
        """
        @desc   Initialize the Vector object
        @param  components  Components of the Vector object 
        @see
        """
        self.magnitude = math.sqrt(sum(x**2 + y**2 + z**2))
        self.direction = [self.x, self.y, self.z] / self.magnitude 

    def multiply(self, number):
        """
        @desc   Multiply the vector by a number
        @param  number  The number by which the vector is multiplied
        @see
        """
        return [self.x, self.y, self.z] * number

    def divide(self, number):
        """
        @desc   Divide the vector by a number
        @param  number  The number by which the vector is divided
        @see
        """
        return [self.x, self.y, self.z] / number

    def add(self, other_vector):
        """
        @desc   Add the vector to another vector
        @param  other_vector  The vector to which the original vector is added
        @see
        """
        return [self.x, self.y, self.z] + other_vector

    def subtract(self, other_vector):
        """
        @desc   Subtract the vector by another vector
        @param  other_vector  The vector which the original vector is subtracted by
        @see
        """
        return [self.x, self.y, self.z] - other_vector

    def dot_product(self, other_vector):
        """
        @desc   Get the dot product of the vector and another vector
        @param  other_vector  The vector with which the original vector is operated on
        @see
        """
        return np.dot([self.x, self.y, self.z], other_vector)

    def cross_product(self, other_vector):
        """
        @desc   Get the cross product of the vector and another vector
        @param  other_vector  The vector with which the original vector is operated on
        @see
        """
        return np.cross([self.x, self.y, self.z], other_vector)
