from encoding.representations import MAPF


def read_instance(instance_file_name: str) -> MAPF:
    with open(instance_file_name, "r") as f:
        data = f.readlines()
        # get range_x, range_y and K
        ranges = data[0].split(" ")
        range_x = int(ranges[0])
        range_y = int(ranges[1])
        K = int(data[1])
        # get starts and goals for every agent
        agents = list(range(K))
        starts = []
        goals = []
        for i in range(2, K + 2):
            coordinates_strings = data[i].split(" ")
            start = (int(coordinates_strings[0]), int(coordinates_strings[1]))
            goal = (int(coordinates_strings[2]), int(coordinates_strings[3]))
            starts.append(start)
            goals.append(goal)
        # get L and coordinates for every obstacle
        L = int(data[K + 2])
        obstacles = []
        for j in range(K + 3, L + K + 3):
            coordinates_strings = data[j].split(" ")
            obstacle = (int(coordinates_strings[0]), int(coordinates_strings[1]))
            obstacles.append(obstacle)
        # make instance
        instance = MAPF(range_x, range_y, agents, starts, goals, obstacles)
        return instance
