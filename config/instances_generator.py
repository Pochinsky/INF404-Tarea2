from random import randint


def generate_starts_goals(K: int, range_x: int, range_y: int) -> tuple[list, list]:
    starts = []
    goals = []
    for _ in range(K):
        flag = True
        while flag:
            start = (randint(0, range_x - 1), randint(0, range_y - 1))
            goal = (randint(0, range_x - 1), randint(0, range_y - 1))
            if start not in starts and goal not in goals and start != goal:
                starts.append(start)
                goals.append(goal)
                flag = False
    return (starts, goals)


def generate_obstacles(L: int, range_x: int, range_y: int) -> list[tuple]:
    obstacles = []
    for _ in range(L):
        flag = True
        while flag:
            obstacle = (randint(0, range_x - 1), randint(0, range_y - 1))
            if obstacle not in obstacles:
                obstacles.append(obstacle)
                flag = False
    return obstacles


def generate_single_instance(
    range_x: int, range_y: int, K: int, L: int, file_path: str
):
    with open(file_path, "w") as f:
        f.write("{} {}\n{}\n".format(range_x, range_y, K))
        starts, goals = generate_starts_goals(K, range_x, range_y)
        for i in range(K):
            f.write(
                "{} {} {} {}\n".format(
                    starts[i][0], starts[i][1], goals[i][0], goals[i][1]
                )
            )
        f.write("{}\n".format(L))
        obstacles = generate_obstacles(L, range_x, range_y)
        for obstacle in obstacles:
            f.write("{} {}\n".format(obstacle[0], obstacle[1]))
