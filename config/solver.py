from pysat.solvers import Glucose3
from pysat.formula import CNF


def sat_solver(formula: CNF):
    solver = Glucose3()
    solver.append_formula(formula)
    if solver.solve():
        model = solver.get_model()
        return model
    return False
