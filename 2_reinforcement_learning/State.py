class State:
    'Defined state of cell in grid world'
    def __init__(self, pos=(0,0), reward= -1, movable=True, absorbing=False, agent_present=False):
        self.pos = pos
        self.reward = reward
        self.movable = movable
        self.absorbing = absorbing
        self.agent_present = agent_present

    def __str__(self):
        return f"{self.pos} reward: {self.reward} | movable: {self.movable} | absorbing: {self.absorbing}"
    
    def print_cell(self):
        'pretty print cell according to state attributes'
        cell = str(self.reward)
        # wall
        if not self.movable:
            cell = f"|{cell}|"
        # agent is present
        elif self.agent_present:
            cell = f"({cell})*"
        return cell