class Agent:
    def __init__(self, pos=[0,0]):
        self.current_pos = pos
        print(self.current_pos)

    def __str__(self):
        return f"Current position of agent: {self.current_pos}"