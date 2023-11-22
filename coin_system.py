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
    def apply(self, state_set: list, current_state: State) -> State:
        if state_set[0] is current_state:
            return state_set[1]
        return state_set[0]

class CoinSystem(System):
    """ Coin System Object."""
    def __init__(self):
        super().__init__(
            system_name = "Coin System",
            state_set = [State(state_name='Heads'), State(state_name="Tails")],
            initial_condition = State(state_name='Heads'),
            current_state = State(state_name='Heads'),
            laws_of_motion = [LawOfStasis(), LawOfFlip()]
        )

        self.initial_condition = random.choice(self.state_set)
        self.current_state = self.initial_condition
