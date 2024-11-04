from encoding.functions import at, shift, finalState


class MAPF:
    actions = ["up", "down", "left", "right", "wait"]
    directions = {
        "up": (0, 1),
        "down": (0, -1),
        "left": (-1, 0),
        "right": (1, 0),
        "wait": (0, 0),
    }
    at_vars = []
    shift_vars = []
    finalState_vars = []

    def __init__(
        self,
        range_x: int,
        range_y: int,
        agents: list[int],
        starts: list[tuple[int, int]],
        goals: list[tuple[int, int]],
        obstacles: list[tuple[int, int]],
    ):
        self.range_x = range_x
        self.range_y = range_y
        self.agents = agents
        self.starts = starts
        self.goals = goals
        self.obstacles = obstacles
        self.V = [(x, y) for x in range(range_x) for y in range(range_y)]

    def set_variables(self, T: int):
        # get vars from at, shift and finalState
        at_vars = at(self, T)
        shift_vars = shift(self, T)
        finalState_vars = finalState(self, T)
        # define index for every var for PySAT solver
        at_vars_index = list(range(0, len(at_vars)))
        shift_vars_index = list(range(len(at_vars), len(at_vars) + len(shift_vars)))
        finalState_vars_index = list(
            range(
                len(at_vars) + len(shift_vars),
                len(at_vars) + len(shift_vars) + len(finalState_vars),
            )
        )
        at_vars_indexed = list(zip(at_vars_index, at_vars))
        shift_vars_indexed = list(zip(shift_vars_index, shift_vars))
        finalState_vars_indexed = list(zip(finalState_vars_index, finalState_vars))
        self.at_vars = at_vars_indexed
        self.shift_vars = shift_vars_indexed
        self.finalState_vars = finalState_vars_indexed


"""
    # set formula
    def set_formula(self, T: int):
        for r in self.agents:
            # Add starts vertex
            start_x, start_y = self.starts[r]
            self.formula.append([self.at(r, start_x, start_y, 0, T)])
            # Goal achievement
            goal_x, goal_y = self.goals[r]
            self.formula.append([self.at(r, goal_x, goal_y, T, T)])
        for x in range(self.range_x):
            for y in range(self.range_y):
                for t in range(T + 1):
                    # Obstacles conflicts
                    if (x, y) in self.obstacles:
                        self.formula.append(
                            [-self.at(r, x, y, t, T) for r in self.agents]
                        )
                    # Vertex conflicts
                    agents_at_same_time = [self.at(r, x, y, t, T) for r in self.agents]
                    if len(agents_at_same_time) > 1:
                        self.formula.extend(
                            [
                                [-agents_at_same_time[i], -agents_at_same_time[j]]
                                for i in range(len(agents_at_same_time))
                                for j in range(i + 1, len(agents_at_same_time))
                            ]
                        )
                    # A single action per agent can be performed at each time instant
                    if t > 0:
                        self.formula.append(
                            [self.shift(x, y, a, t, T) for a in self.actions]
                        )
                        self.formula.extend(
                            [
                                [
                                    -self.shift(x, y, a1, t, T),
                                    -self.shift(x, y, a2, t, T),
                                ]
                                for a1 in self.actions
                                for a2 in self.actions
                                if a1 != a2
                            ]
                        )
                    # Swap conflicts
                    if t < T:
                        for r1 in self.agents:
                            for r2 in self.agents:
                                if r1 != r1:
                                    for _, (dx, dy) in self.directions.items():
                                        if (
                                            x + dx >= 0
                                            and x + dx < self.range_x
                                            and y + dy >= 0
                                            and y + dy < self.range_y
                                        ):
                                            self.formula.append(
                                                [
                                                    -self.at(r1, x, y, t),
                                                    -self.at(r2, x + dx, y + dy, t),
                                                    -self.at(r1, x + dx, y + dy, t + 1),
                                                    -self.at(r2, x, y, t + 1),
                                                ]
                                            )
"""
