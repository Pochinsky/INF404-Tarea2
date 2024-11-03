from random import randint
from data.encoding import Coordenate, Agent


def generate_agents(K: int, range_x: int, range_y: int) -> list[Agent]:
    agents = []
    unavailable_starts = []
    unavailable_goals = []
    for _ in range(K):
        flag = True
        while flag:
            start = (randint(0, range_x - 1), randint(0, range_y - 1))
            goal = (randint(0, range_x - 1), randint(0, range_y - 1))
            if (
                start not in unavailable_starts
                and goal not in unavailable_goals
                and start == goal
            ):
                agent = Agent(start, goal)
                agents.append(agent)
                unavailable_starts.append(start)
                unavailable_goals.append(goal)
                flag = False
    return agents


def generate_obstacles(L: int, range_x: int, range_y: int) -> list[Coordenate]:
    obstacles = []
    unavailable_coordenates = []
    for _ in range(L):
        flag = True
        while flag:
            coordenate = (randint(0, range_x - 1), randint(0, range_y - 1))
            if coordenate not in unavailable_coordenates:
                obstacle = Coordenate(coordenate[0], coordenate[1])
                obstacles.append(obstacle)
                unavailable_coordenates.append(coordenate)
                flag = False
    return obstacles


def generate_single_instance(
    range_x: int, range_y: int, K: int, L: int, file_path: str
) -> None:
    with open(file_path, "w") as f:
        f.write("{} {}\n{}\n".format(range_x, range_y, K))
        agents = generate_agents(K, range_x, range_y)
        for agent in agents:
            f.write(
                "{} {} {} {}\n".format(
                    agent.start.x, agent.start.y, agent.goal.x, agent.goal.y
                )
            )
        f.write("{}\n".format(L))
        obstacles = generate_obstacles(L, range_x, range_y)
        for obstacle in obstacles:
            f.write("{} {}\n".format(obstacle.x, obstacle.y))
