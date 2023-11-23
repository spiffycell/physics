from classical_mechanics import System, State
from laws import LawOfStasis, LawOfFlip

class CoinSystem(System):
    """ Coin System Object."""
    def __init__(self):
        """ Initialize the Coin System."""
        super().__init__(
            system_name = "Coin System",
            system_space = [],
            state_space = [State(state_name='Heads'), State(state_name="Tails")],
            initial_condition = State(state_name='Heads'),
            current_state = State(state_name='Heads'),
            prior_state = State(state_name='Heads'),
            laws_of_motion = [LawOfStasis(), LawOfFlip()]
        )

        self.initial_condition = random.choice(self.state_space)
        self.current_state = self.initial_condition
        self.prior_state = None
