class Agent:
    'Agent (player) of the game. Assuming that player will start from [0,0]'
    def __init__(self, pos=(0,0)):
        self.pos = pos
        print(self.pos)

    def __str__(self):
        return f"Current position of agent: {self.pos}"

    def move(self, direction):
        'move agent in a direction'
        row=0; col=0
        if direction == 'north':
            row = -1
        elif direction == 'south':
            row = 1
        elif direction == 'east':
            col = 1
        elif direction == 'west':
            col = -1
         
        self.pos = (self.pos[0]+row, self.pos[1]+col)
        print(f"Moved {direction} to: {self.pos}")

        return self.pos
    
    # def current_position(self):
    #     return self.current_pos