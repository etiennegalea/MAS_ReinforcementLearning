class Agent:
    'Agent (player) of the game. Assuming that player will start from [0,0]'
    def __init__(self, pos=(0,0)):
        self.pos = pos
        print(self.pos)

    def __str__(self):
        return f"Current position of agent: {self.pos}"

    def move(self, direction):
        'move agent in a direction'
        x=0; y=0
        if direction == 'up':
            x = -1
        elif direction == 'down':
            x = 1
        elif direction == 'right':
            y = 1
        elif direction == 'left':
            y = -1
         
        self.pos = (self.pos[0]+x, self.pos[1]+y)
        print(f"Moved {direction} to: {self.pos}")

        return self.pos
    
    # def current_position(self):
    #     return self.current_pos