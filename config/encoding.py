class MAPF:
    actions = ["up", "down", "left", "right", "wait"]
    directions = {
        "up": (0, 1),
        "down": (0, -1),
        "left": (-1, 0),
        "right": (1, 0),
        "wait": (0, 0),
    }

    def __init__(
        self,
        range_x: int,
        range_y: int,
        agents: list[int],
        starts: list[tuple],
        goals: list[tuple],
        obstacles: list[tuple],
    ):
        self.range_x = range_x
        self.range_y = range_y
        self.agents = agents
        self.starts = starts
        self.goals = goals
        self.obstacles = obstacles


# CONSTRAINTS
# C1 (shift variables): cada vertice u shiftea a exactamente uno de sus vecinos v en cada paso t
# C2 (vertex conflicts): dos o mas agentes no pueden ocupar el mismo vertice u en un paso t
