from utils.files_reader import read_instance
# from utils.instances_generator import generate_single_instance
from solver.solver import sat_solver
from encoding.rules import dynamics_at_clauses

# generate_single_instance(5, 5, 2, 2, "./data/test_instance.txt")

T = 10

mapf = read_instance("./data/test_instance.txt")
mapf.set_variables(T)
dynamics_at_clauses(mapf, T)
# mapf.set_formula(T)
# model = sat_solver(mapf.formula)
# print(mapf.formula.clauses)
