def d(u: tuple[int, int], v: tuple[int, int]) -> int:
    u_x, u_y = u
    v_x, v_y = v
    dx = abs(u_x - v_x)
    dy = abs(u_y - v_y)
    return dx + dy


def Feasible(mapf_instance, r: int, t: int, T: int) -> list[tuple[int, int]]:
    start_r = mapf_instance.starts[r]
    goal_r = mapf_instance.goals[r]
    feasibly_reached_vertices = []
    for u in mapf_instance.V:
        if u != start_r and u != goal_r:
            d_start_to_u = d(start_r, u)
            d_u_to_goal = d(u, goal_r)
            if d_start_to_u <= t and d_u_to_goal <= T - t:
                feasibly_reached_vertices.append(u)
    return feasibly_reached_vertices


def at(mapf_instance, T: int) -> list[tuple[int, tuple[int, int], int]]:
    at_variables = []
    for r in mapf_instance.agents:
        for t in range(T + 1):
            V_feasibly = Feasible(mapf_instance, r, t, T)
            for u in V_feasibly:
                at_variables.append((r, u, t))
    return at_variables


def shift(mapf_instance, T: int) -> list[tuple]:
    shift_variables = [
        (u, a, t)
        for u in mapf_instance.V
        for a in mapf_instance.actions
        for t in range(T + 1)
    ]
    return shift_variables


def finalState(mapf_instance, T: int):
    finalState_variables = [(r, t) for r in mapf_instance.agents for t in range(T + 1)]
    return finalState_variables


def delta(mapf_instance):
    delta_variables = [
        (a, u, v)
        for a in mapf_instance.actions
        for u in mapf_instance.V
        for v in mapf_instance.V
    ]
    return delta_variables


def cost_to_go(mapf_instance):
    cost_to_go_vars = []
    for u in mapf_instance.V:
        for r, goal_r in enumerate(mapf_instance.goals):
            c = d(u, goal_r)
            cost_to_go_vars.append((r, u, c))
    return cost_to_go_vars


def free(mapf_instance):
    return list(mapf_instance.V)


def obstacle(mapf_instance):
    return list(mapf_instance.V)
