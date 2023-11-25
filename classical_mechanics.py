"""
Notes for The Theoretical Minimum.

Links for courses:
- https://theoreticalminimum.com/courses
"""
# standard imports 
from pydantic import BaseModel, Field
import random
from typing import List

# local imports
from analysis import Vector

# macros
GRAVITY_ACCEL = 9.81

# classes
class State(BaseModel):
    """ 
    @desc   State object.
    @param
    @return
    @see
    """
    state_name: str

class LawOfMotion(BaseModel):
    """ 
    @desc   Law Of Motion object.
    @param
    @return
    @see
    """
    class Config:
        arbitrary_types_allowed = True

    def apply(self, state: State):
        raise NotImplementedError("Subclasses must implement the apply method.")

class InertialFrame(BaseModel):
    """ 
    @desc   Inertial Frame Of Reference object.
    @param
    @return
    @see
    """
    time: float = Field(..., description="Time in seconds")
    x: float = Field(..., description="x-coordinate in meters")
    y: float = Field(..., description="y-coordinate in meters")
    z: float = Field(..., description="z-coordinate in meters")

class System(BaseModel):
    """ 
    @desc   System object.
    @param
    @return
    @see
    """
    system_name: str
    mass: float
    position: Vector
    velocity: Vector
    state_set: List[State]
    initial_condition: State
    current_state: State
    laws_of_motion: List[LawOfMotion]
    subsystems: List["System"]
    kinetic_energy: float
    potential_energy: float

    def __init__(self):
        """ Initialize System."""
        self.kinetic_energy = get_kinetic_energy() 
        self.potential_energy = get_potential_energy()

    def get_kinetic_energy(self):
        """ Kinetic Energy of the system."""
        kinetic_energy = 1/2 * self.mass * (velocity.magnitude)^2
        return kinetic_energy

    def get_potential_energy(self):
        """ Potential Energy of the system."""
        potential_energy = self.mass * GRAVITY_ACCEL * self.position.z
        return potential_energy
