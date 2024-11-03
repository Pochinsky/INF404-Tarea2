class Coordenate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Agent:
    def __init__(self, start: tuple[int, int], goal: tuple[int, int]):
        self.start = Coordenate(start[0], start[1])
        self.goal = Coordenate(goal[0], goal[1])
        self.position = self.start
