from classical_mechanics import State, System
from laws import LawOfStasis, LawOfCycle, LawOfConservedQuantity, LawOfRoll

class DieSystem(System):
    """ Die System Object."""
    def __init__(self):
        super().__init__(
            system_name = "Die System",
            state_space = [State(state_name='One'), State(state_name='Two'), State(state_name='Three'), \
                    State(state_name='Four'), State(state_name='Five'), State(state_name='Six')],
            initial_condition = State(state_name='One'),
            current_state = State(state_name='One'),
            prior_state = State(state_name='One'),
            laws_of_motion = [LawOfStasis(), LawOfCycle(), LawOfConservedQuantity(), LawOfRoll()]
        )
        self.initial_condition = random.choice(self.state_space)
        self.current_state = self.initial_condition
        self.prior_state = None
