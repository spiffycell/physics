""" Enumeration of Laws which some systems are subject to."""
from classical_mechanics import LawOfMotion

class LawOfStasis(LawOfMotion):
    """
    Law of Motion: Over time, the State stays the same.

    example: sigma(t+1) = sigma(t)

    @param  current_state   The current state or configuration of the given system      
    @return new_state       The new state or configuration of the system after the law is applied
    @see
    """
    def apply(self, current_state: State) -> State:
        if current_state:
            new_state = current_state
            return new_state

class LawOfFlip(LawOfMotion):
    """
    Law of Motion: Over time, the State transitions for state set of size two.

    example: sigma(t+1) = -(sigma(t)) 

    @param  state_space     The set of possible states for a given system 
    @param  current_state   The current state or configuration of the given system      
    @return new_state       The new state or configuration of the system after the law is applied
    @see
    """
    def apply(self, state_space: list, current_state: State) -> State:
        if state_space[0] is current_state:
            new_space = state_space[1]
            return new_space
        new_space = state_space[0]
        return new_space

class LawOfCycle(LawOfMotion):
    """
    Law of Motion: Over time, the State transitions from one to the next in ordered sequence.

    @param  state_space     The set of possible states for a given system 
    @param  current_state   The current state or configuration of the given system      
    @return new_state       The new state or configuration of the system after the law is applied
    @return
    @see
    """
    def apply(self, state_space: list, current_state: State) -> State:
        for index in range(0, len(state_space)):
            if state_space[index] == current_state:
                new_state = state_space[(index + 1) % 6]
                return new_state

class LawOfConservedQuantity(LawOfMotion):
    """
    Law of Motion: Over time, the State transitions from one to the next for a subset of states in ordered sequence.
    Note: if you start with a state of One, for instance, you will never get to state Four, and vice versa

    Systems subject to this law can be said to have a Conserved Quantity
    In this example, if i set the current_state and give it a conserved quantity of 0, it will transition into itself
    if i set to a conserved quantity of 1, it will transition to one other state, then back to itself.

    @param state_space          The set of possible states for a given system 
    @param current_state        The current state or configuration of the given system      
    @param conserved_quantity   The conserved quantity of the system. size of an iterative cycle, zero-indexed. 
    @param position             The current_state position relative to the conserved_quantity 
    @return State               The state that is transitioned to as a result of applying the law
    @see
    """
    def apply(self, state_space: list, current_state: State, conserved_quantity: int, position: int) -> State:
        for index in range(0, len(state_space)):
            # find where in the array the current state is
            if state_space[index] == current_state:
                # if the position of the state isn't at the end of the cycle 
                if position < conserved_quantity:
                    # keep moving forward in the cycle
                    return state_space[index + 1]
                # else, if it's at the end of the cycle
                elif position == conserved_quantity:
                    # circle back to the beginning of the cycle
                    # note that the conserved_quantity is equal to the distance 
                    # between the first and final indices of the cycle
                    return state_space[index - conserved_quantity]

class LawOfRoll(LawOfMotion):
    """
    Law of Motion: Over time, the State transitions from one to one of six states \
            (including the current state).

    @param  state_space The set of all possible states for a given system
    @return new_state   The new state or configuration of the system after the law is applied
    @see
    """
    def apply(self, state_space: list) -> State:
        new_state = random.choice(state_space)
        return new_state

class LawOfSkipForward(LawOfMotion):
    """
    Law of Motion: Over time, the State transitions forward from one even-indexed State \
            to the next, or odd-indexed State to the next.

    @param  state_space The set of all possible states for a given system
    @return new_state   The new state or configuration of the system after the law is applied
    @see
    """
    def apply(self, state_space: list, current_state: State) -> State:
        """ Apply the Law Of Skip Forward."""
        for index in range(0, len(state_space)):
            if state_space[index] == current_space:
                new_state = state_space[index + 2] 
                return new_state

