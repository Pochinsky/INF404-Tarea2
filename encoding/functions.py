def d(u: tuple[int, int], v: tuple[int, int]) -> int:
    u_x, u_y = u
    v_x, v_y = v
    dx = abs(u_x - v_x)
    dy = abs(u_y - v_y)
    return dx + dy


def Feasible(mapf_instance, a: int, t: int, T: int) -> list[tuple[int, int]]:
    start_a = mapf_instance.starts[a]
    goal_a = mapf_instance.goals[a]
    feasibly_reached_vertices = []
    for u in mapf_instance.V:
        if u != start_a and u != goal_a:
            d_start_to_u = d(start_a, u)
            d_u_to_goal = d(u, goal_a)
            if d_start_to_u <= t and d_u_to_goal <= T - t:
                feasibly_reached_vertices.append(u)
    return feasibly_reached_vertices


def at(mapf_instance, T: int) -> list[tuple[int, tuple[int, int], int]]:
    at_variables = []
    for a in mapf_instance.agents:
        for t in range(T + 1):
            V_feasibly = Feasible(mapf_instance, a, t, T)
            for u in V_feasibly:
                at_variables.append((a, u, t))
    return at_variables


def shift(mapf_instance, T: int) -> list[tuple]:
    shift_variables = [
        (u, v, t)
        for u in mapf_instance.V
        for v in mapf_instance.V
        for t in range(T + 1)
    ]
    return shift_variables


def finalState(mapf_instance, T: int):
    finalState_variables = [(a, t) for a in mapf_instance.agents for t in range(T + 1)]
    return finalState_variables
