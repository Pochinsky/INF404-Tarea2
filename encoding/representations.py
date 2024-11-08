from pysat.formula import CNF
from encoding.functions import at, shift, finalState, delta, cost_to_go, free, obstacle


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
    delta_vars = []
    cost_vars = []
    free_vars = []
    obstacle_vars = []
    formula = CNF()

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
        delta_vars = delta(self)
        cost_vars = cost_to_go(self)
        free_vars = free(self)
        obstacle_vars = obstacle(self)
        # define lenghts fo lists of vars
        L_at_vars = len(at_vars)
        L_shift_vars = len(shift_vars)
        L_finalState_vars = len(finalState_vars)
        L_delta_vars = len(delta_vars)
        L_cost_vars = len(cost_vars)
        L_free_vars = len(free_vars)
        L_obstacle_vars = len(obstacle_vars)
        # define index for every var for PySAT solver
        at_vars_index = list(range(0, L_at_vars))
        shift_vars_index = list(range(L_at_vars, L_at_vars + L_shift_vars))
        finalState_vars_index = list(
            range(
                L_at_vars + L_shift_vars,
                L_at_vars + L_shift_vars + L_finalState_vars,
            )
        )
        delta_vars_index = list(
            range(
                L_at_vars + L_shift_vars + L_finalState_vars,
                L_at_vars + L_shift_vars + L_finalState_vars + L_delta_vars,
            )
        )
        cost_vars_index = list(
            range(
                L_at_vars + L_shift_vars + L_finalState_vars + L_delta_vars,
                L_at_vars
                + L_shift_vars
                + L_finalState_vars
                + L_delta_vars
                + L_cost_vars,
            )
        )
        free_vars_index = list(
            range(
                L_at_vars
                + L_shift_vars
                + L_finalState_vars
                + L_delta_vars
                + L_cost_vars,
                L_at_vars
                + L_shift_vars
                + L_finalState_vars
                + L_delta_vars
                + L_cost_vars
                + L_free_vars,
            )
        )
        obstacle_vars_index = list(
            range(
                L_at_vars
                + L_shift_vars
                + L_finalState_vars
                + L_delta_vars
                + L_cost_vars
                + L_free_vars,
                L_at_vars
                + L_shift_vars
                + L_finalState_vars
                + L_delta_vars
                + L_cost_vars
                + L_free_vars
                + L_obstacle_vars,
            )
        )
        # associate index to respective var
        at_vars_indexed = list(zip(at_vars_index, at_vars))
        shift_vars_indexed = list(zip(shift_vars_index, shift_vars))
        finalState_vars_indexed = list(zip(finalState_vars_index, finalState_vars))
        delta_vars_indexed = list(zip(delta_vars_index, delta_vars))
        cost_vars_indexed = list(zip(cost_vars_index, cost_vars))
        free_vars_indexed = list(zip(free_vars_index, free_vars))
        obstacle_vars_indexed = list(zip(obstacle_vars_index, obstacle_vars))
        # set lists of variables
        self.at_vars = at_vars_indexed
        self.shift_vars = shift_vars_indexed
        self.finalState_vars = finalState_vars_indexed
        self.delta_vars = delta_vars_indexed
        self.cost_vars = cost_vars_indexed
        self.free_vars = free_vars_indexed
        self.obstacle_vars = obstacle_vars_indexed
