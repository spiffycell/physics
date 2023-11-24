""" Classes and methods associated with Analysis."""
# imports
from pydantic import BaseModel
from typing import List
import math

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
