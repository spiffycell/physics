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
        """ Set the Configuration for general Law Of Motion."""
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
    To predict the future in a classical system, we need to know two things:
    - what are its initial conditions (with perfect knowledge)?
        - minor deviations in reality from our calculations could blow up in our face
    - what are its laws of motion?

    Knowing just how imperfect your knowledge is helps you determine HOW FAR 
    into the future or HOW far into the past you can predict or retrodict

    @desc   System object.
    @param  BaseModel from pydantic
    @see
    """
    system_name: str
    state_space: List[State]
    initial_condition: State
    current_state: State
    prior_state: State
    laws_of_motion: List[LawOfMotion]
