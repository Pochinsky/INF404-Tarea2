def shift_cond_to_at(mapf_instance, T: int):
    shift_vars_indexes, shift_vars = list(zip(*mapf_instance.shift_vars))
    to_add_to_clauses = []
    for i, x in enumerate(shift_vars):
        # x = (u, a, t), u: vertex, a: action, t: step
        if x[2] == T - 1:
            to_add_to_clauses.append(-shift_vars_indexes[i])
    return to_add_to_clauses


def at_cond_to_itself(indexes, vars, T):
    to_add_to_clauses = []
    for i, x in enumerate(vars):
        if x[2] == T - 1:
            to_add_to_clauses.append(-indexes[i])
    return to_add_to_clauses


def dynamics_at_clauses(mapf_instance, T: int):
    """
    Note:

    ASP rules:
    at(R,X,Y,T) :- shift(Xp,Yp,A,T-1), at(R,Xp,Yp,T-1), delta(A,Xp,Yp,X,Y), cost_to_go(R,X,Y,C), T + C <= bound

    Therefore, clause are:
    at(R,X,Y,T) or -shift(Xp,Yp,A,T-1) or -at(R,Xp,Yp,T-1) or -delta(A,Xp,Yp,X,Y) or -cost_to_go(R,X,Y,C) or -(T + C <= bound)
    """
    clauses = []
    for at_var in mapf_instance.at_vars:
        # at_var = (i, (r, u, t))
        clause = [at_var[0]]
        at_var_r = at_var[1][0]
        at_var_u = at_var[1][1]
        at_var_t = at_var[1][2]
        # add -shift(Xp,Yp,A,T-1)
        for shift_var in mapf_instance.shift_vars:
            # shift_var = (i, (u, a, t))
            shift_var_t = shift_var[1][2]
            if at_var_t == 0:
                if shift_var_t == 0:
                    clause.append(-shift_var[0])
            else:
                if shift_var_t == at_var_t - 1:
                    clause.append(-shift_var[0])
        # add -at(R,Xp,Yp,T-1)
        for at_var_aux in mapf_instance.at_vars:
            at_var_aux_t = at_var_aux[1][2]
            if at_var_t == 0:
                if at_var_aux_t == 0:
                    clause.append(-at_var_aux[0])
            else:
                if at_var_aux_t == at_var_t - 1:
                    clause.append(-at_var_aux[0])
        # add -delta(A,Xp,Yp,X,Y)
        for delta_var in mapf_instance.delta_vars:
            # delta_var = (i, (a, u, v))
            delta_var_v = delta_var[1][2]
            if at_var_u == delta_var_v:
                clause.append(-delta_var[0])
        # add -cost_to_go(R,X,Y,C) and -(T + C <= bound)
        for cost_var in mapf_instance.cost_vars:
            # cost_var = (i, (r, u, c))
            cost_var_r = cost_var[1][0]
            cost_var_u = cost_var[1][1]
            cost_var_c = cost_var[1][2]
            if (
                at_var_u == cost_var_u
                and at_var_r == cost_var_r
                and at_var_t + cost_var_c <= T
            ):
                clause.append(-cost_var[0])
        clauses.append(clause)
    return clauses


def free_for_moves_specs(mapf_instance):
    """
    Note:

    ASP rules:
    free(X,Y) :- rangeX(X), rangeY(Y), not obstacle(X,Y)

    Therefore, clauses are:
    free(X,Y) or -rangeX(X) or -rangeY(Y) or obstacle(X,Y)
    """
    clauses = []
    free_vars = mapf_instance.free_vars
    obstacle_vars = mapf_instance.obstacle_vars
    for i, u in enumerate(mapf_instance.V):
        clause = [free_vars[i][0]]
        if u in mapf_instance.obstacles:
            clause.append(obstacle_vars[i][0])
        else:
            clause.append(-obstacle_vars[i][0])
        clauses.append(clause)
    return clauses


def moves_specification_clauses(mapf_instance):
    """
    Note:

    ASP rules:
    delta(left,X,Y,X-1,Y) :- rangeX(X), rangeX(X-1), rangeY(Y), free(X,Y)
    delta(up,X,Y,X,Y+1) :- rangeX(X), rangeY(Y), rangeY(Y+1), free(X,Y)
    delta(down,X,Y,X,Y-1) :- rangeX(X), rangeY(Y), rangeY(Y-1), free(X,Y)
    delta(wait,X,Y,X,Y) :- rangeX(X), rangeY(Y), free(X,Y)

    Therefore, clauses are:
    delta(left,X,Y,X-1,Y) or -rangeX(X) or -rangeX(X-1) or -rangeY(Y) or -free(X,Y)
    delta(up,X,Y,X,Y+1) or -rangeX(X) or -rangeY(Y) or -rangeY(Y+1) or -free(X,Y)
    delta(down,X,Y,X,Y-1) or -rangeX(X) or -rangeY(Y) or -rangeY(Y-1) or -free(X,Y)
    delta(wait,X,Y,X,Y) or -rangeX(X) or -rangeY(Y) or -free(X,Y)
    """
