class State:
    'Defined state of cell in grid world'
    def __init__(self, pos=[0,0], reward= -1, movable=True, absorbing=False, agent_present=False):
        self.pos = pos
        self.reward = reward
        self.movable = movable
        self.absorbing = absorbing
        self.v_pi = []
        self.v_pi_mean = 0
        # q_pi(s,a): action-state values
        self.q = {
            'north': 0.0,
            'south': 0.0,
            'east': 0.0,
            'west': 0.0,
        }

    def __str__(self):
        return f"{self.pos} reward: {self.reward} | movable: {self.movable} | absorbing: {self.absorbing}"
    
    def print_cell(self, to_show, agent_present=False):
        'pretty print cell according to state attributes'

        if to_show == 'reward':
            cell = str(self.reward)
        elif to_show == 'q':
            direction = max(self.q, key=lambda k: self.q[k])
            # set print signs for readability
            if direction == 'north':
                sign = '^'
            elif direction == 'south':
                sign = 'v'
            elif direction == 'east':
                sign = '>'
            elif direction == 'west':
                sign = '<'
                
            cell = str(f"{sign} ({round(self.q[direction],1)})")
        elif to_show == 'v':
            cell = str(self.v_pi)
        # wall
        if not self.movable:
            cell = f"|{cell}|"
        elif self.absorbing:
            cell = f"[{cell}]*"

        # agent is present
        if agent_present:
            cell = f"<{cell}>"
        return cell