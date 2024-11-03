class Coordenate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Agent:
    def __init__(self, start: tuple[int, int], goal: tuple[int, int]):
        self.start = Coordenate(start[0], start[1])
        self.goal = Coordenate(goal[0], goal[1])
        self.position = self.start


class MAPF:
    def __init__(
        self,
        range_x: int,
        range_y: int,
        agents: list[Agent],
        obstacles: list[Coordenate],
    ):
        self.range_x = range_x
        self.range_y = range_y
        self.agents = agents
        self.obstacles = obstacles

    def show_details(self):
        print("Multi-Agent Path Finding\n")
        print("range_x =", self.range_x)
        print("range_y =", self.range_y)
        print("number of agents =", len(self.agents))
        print("number of obstacles =", len(self.obstacles))
