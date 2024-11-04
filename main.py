from utils.files_reader import read_instance
from config.solver import sat_solver

# from utils.instances_generator import generate_single_instance

# generate_single_instance(5, 5, 2, 2, "./data/test_instance.txt")

T = 10

mapf = read_instance("./data/test_instance.txt")
mapf.set_variables(T)
# mapf.set_formula(T)
# model = sat_solver(mapf.formula)
# print(mapf.formula.clauses)
