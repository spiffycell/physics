"""
Three sided coin system.
Here we introduce allowable and nonallowable laws.
"""
from classical_mechanics import System, State
from laws import LawOfStasis, LawOfFlip

class ThreeSidedCoin(System):
    """ Object for ThreeSidedCoin."""
    def __init__(self):
        """ Initialize Three-Sided Coin System."""
        super().__init__(
            system_name = "Three-Sided Coin",
            state_space = [
                State(state_name='Heads'), \
                State(state_name="Tails"), \
                State(state_name="Edge")
            ],
            initial_condition = State(state_name='Heads'),
            current_state = State(state_name='Heads'),
            prior_state = State(state_name='Heads'),
            laws_of_motion = [LawOfStasis(), LawOfFlip()]
        )

        self.initial_condition = random.choice(self.state_space)
        self.current_state = self.initial_condition
        self.prior_state = None
