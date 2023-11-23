""" Point Particle System."""
from classical_mechanics import State, System
from laws import LawOfStasis, LawOfCycle, LawOfConservedQuantity, LawOfRoll

class Particle(System):
    """ Particle Object."""
    def __init__(self):
        """ Initialize the Die System."""
        super().__init__(
            system_name = "Particle",
            state_space = [],
            initial_condition = State(state_name="Config1"),
            current_state = State(state_name="Config2"),
            prior_state = State(state_name="Config3"),
            laws_of_motion = []
        )
        self.initial_condition = random.choice(self.state_space)
        self.current_state = self.initial_condition
        self.prior_state = None
