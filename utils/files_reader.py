from config.encoding import Agent, Coordenate, MAPF


def read_instance(instance_file_name: str) -> MAPF:
    with open(instance_file_name, "r") as f:
        data = f.readlines()
        # get range_x, range_y and K
        ranges = data[0].split(" ")
        range_x = int(ranges[0])
        range_y = int(ranges[1])
        K = int(data[1])
        # get starts and goals for every agent
        agents = []
        for i in range(2, K + 2):
            coordinates_strings = data[i].split(" ")
            start = (int(coordinates_strings[0]), int(coordinates_strings[1]))
            goal = (int(coordinates_strings[2]), int(coordinates_strings[3]))
            agent = Agent(start, goal)
            agents.append(agent)
        # get L and coordinates for every obstacle
        L = int(data[K + 2])
        obstacles = []
        for j in range(K + 3, L + K + 3):
            coordinates_strings = data[j].split(" ")
            x = int(coordinates_strings[0])
            y = int(coordinates_strings[1])
            obstacle = Coordenate(x, y)
            obstacles.append(obstacle)
        # make instance
        instance = MAPF(range_x, range_y, agents, obstacles)
        return instance
