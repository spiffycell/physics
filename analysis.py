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
    components: List[float]
    magnitude: float
    direction: List[float]

    def __init__(self, components):
        """
        @desc   Initialize the Vector object
        @param  components  Components of the Vector object 
        @see
        """
        self.components = components
        self.magnitude = math.sqrt(sum(x**2 for x in self.components))
        self.direction = self.components / self.magnitude 

    def multiply(self, number):
        """
        @desc   Multiply the vector by a number
        @param  number  The number by which the vector is multiplied
        @see
        """
        return self.components * number

    def divide(self, number):
        """
        @desc   Divide the vector by a number
        @param  number  The number by which the vector is divided
        @see
        """
        return self.components / number

    def add(self, other_vector):
        """
        @desc   Add the vector to another vector
        @param  other_vector  The vector to which the original vector is added
        @see
        """
        return self.components + other_vector

    def subtract(self, other_vector):
        """
        @desc   Subtract the vector by another vector
        @param  other_vector  The vector which the original vector is subtracted by
        @see
        """
        return self.components - other_vector

    def dot_product(self, other_vector):
        """
        @desc   Get the dot product of the vector and another vector
        @param  other_vector  The vector with which the original vector is operated on
        @see
        """
        return np.dot(self.components, other_vector)

    def cross_product(self, other_vector):
        """
        @desc   Get the cross product of the vector and another vector
        @param  other_vector  The vector with which the original vector is operated on
        @see
        """
        return np.cross(self.components, other_vector)
