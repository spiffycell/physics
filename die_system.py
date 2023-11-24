from classical_mechanics import State, System, LawOfMotion, Vector

class LawOfStasis(LawOfMotion):
    """
    Law of Motion: Over time, the State stays the same.

    example: sigma(t+1) = sigma(t)
    """
    def apply(self, current_state: State) -> State:
        if current_state is current_state:
            return current_state

class LawOfCycle(LawOfMotion):
    """
    Law of Motion: Over time, the State transitions from one to the next in ordered sequence.
    """
    def apply(self, state_set: list, current_state: State) -> State:
        for index in range(0, len(state_set)):
            if state_set[index] == current_state:
                new_state = state_set[(index + 1) % 6]
                return new_state

class LawOfConservedQuantity(LawOfMotion):
    """
    Law of Motion: Over time, the State transitions from one to the next for a subset of states in ordered sequence.
    Note: if you start with a state of One, for instance, you will never get to state Four, and vice versa

    Systems subject to this law can be said to have a Conserved Quantity
    In this example, if i set the current_state and give it a conserved quantity of 0, it will transition into itself
    if i set to a conserved quantity of 1, it will transition to one other state, then back to itself.

    I'm able to map the general system of conserved quantities and their dynamics, but need to find a generalized way to
    map specific states to specific conserved quantity types
    """
    def apply(self, state_set: list, current_state: State, conserved_quantity: int) -> State:
        for index in range(0, len(state_set)):
            if state_set[index] == current_state:
                new_state = state_set[(index + 1) % (conserved_quantity + 1)]
                return new_state

class LawOfRoll(LawOfMotion):
    """
    Law of Motion: Over time, the State transitions from one to one of six states (including the current state).
    """
    def apply(self, state_set: list) -> State:
        new_state = random.choice(state_set)
        return new_state

class DieSystem(System):
    """ Die System Object."""
    def __init__(self):
        super().__init__(
            system_name = "Die System",
            state_set = [State(state_name='One'), State(state_name='Two'), State(state_name='Three'), \
                    State(state_name='Four'), State(state_name='Five'), State(state_name='Six')],
            initial_condition = State(state_name='One'),
            current_state = State(state_name='One'),
            laws_of_motion = [LawOfStasis(), LawOfCycle(), LawOfConservedQuantity(), LawOfRoll()],
            position = Vector(time=0, x=0, y=0, z=0),
            velocity = Vector(time=0, x=0, y=0, z=0)
        )
        self.initial_condition = random.choice(self.state_set)
        self.current_state = self.initial_condition
