from classical_mechanics import System, State, LawOfMotion

class LawOfStasis(LawOfMotion):
    """
    Law of Motion: Over time, the State stays the same.

    example: sigma(t+1) = sigma(t)
    """
    def apply(self, current_state: State) -> State:
        if current_state is current_state:
            return current_state

class LawOfFlip(LawOfMotion):
    """
    Law of Motion: Over time, the State transitions for state set of size two.

    example: sigma(t+1) = -(sigma(t)) 
    """
    def apply(self, state_space: list, current_state: State) -> State:
        if state_space[0] is current_state:
            return state_space[1]
        return state_space[0]

class CoinSystem(System):
    """ Coin System Object."""
    def __init__(self):
        super().__init__(
            system_name = "Coin System",
            state_space = [State(state_name='Heads'), State(state_name="Tails")],
            initial_condition = State(state_name='Heads'),
            current_state = State(state_name='Heads'),
            laws_of_motion = [LawOfStasis(), LawOfFlip()]
        )

        self.initial_condition = random.choice(self.state_space)
        self.current_state = self.initial_condition
