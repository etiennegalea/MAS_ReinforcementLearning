class Agent:
    'Agent (player) of the game. Assuming that player will start from [0,0]'
    def __init__(self, pos=(0,0)):
        self.pos = (pos[0],pos[1])
        print(self.pos)

    def __str__(self):
        return f"Current position of agent: {self.pos}"

    def move(self, direction, pos=None):
        'move agent in a direction'

        # if pos is not defined, assume current agent position
        current_pos = self.pos
        if pos is not None:
            current_pos = pos


        row=0; col=0
        if direction == 'north':
            row = -1
        elif direction == 'south':
            row = 1
        elif direction == 'east':
            col = 1
        elif direction == 'west':
            col = -1
         
        new_pos = (current_pos[0]+row, current_pos[1]+col)
        print(f"Moved {direction} to: {new_pos}")

        return new_pos
    
    # def current_position(self):
    #     return self.current_pos