"""
Notes for The Theoretical Minimum.

Links for courses:
- https://theoreticalminimum.com/courses
"""
# imports 
from pydantic import BaseModel
import random
from typing import List

# classes
class State(BaseModel):
    """ 
    @desc   State object.
    @param  BaseModel from pydantic
    @see
    """
    state_name: str

class LawOfMotion(BaseModel):
    """ 
    @desc   Law Of Motion object.
    @param  State of the current System
    @see
    """
    class Config:
        arbitrary_types_allowed = True

    def apply(self, state: State):
        """
        Apply the law of motion
        @desc   Law Of Motion object.
        @param  State of the current System
        @see
        """
        raise NotImplementedError("Subclasses must implement the apply method.")

class System(BaseModel):
    """ 
    @desc   System object.
    @param  BaseModel from pydantic
    @see
    """
    system_name: str
    state_space: List[State]
    initial_condition: State
    current_state: State
    laws_of_motion: List[LawOfMotion]
