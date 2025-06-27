import heapq

def A_Star(graph, start, goal):
    to_explore = []
    heapq.heappush(to_explore, (start.getHeuristic(), id(start), start))

    visited_order = []
    cost = {start.getId(): 0}
    from_vertex = {start.getId(): None}

    while to_explore:
        f_n, _, current = heapq.heappop(to_explore)
        current_vertex = graph.getVertex(current.getId())
        visited_order.append(current_vertex)

        if current_vertex.getId() == goal.getId():
            path = reconstruct_path(from_vertex, goal)
            return path, cost[goal.getId()], visited_order

        for neighbor in current_vertex.getConnections():
            edge_weight = current_vertex.getWeight(neighbor)
            temp_cost = cost[current_vertex.getId()] + edge_weight

            if neighbor.getId() not in cost or temp_cost < cost[neighbor.getId()]:
                cost[neighbor.getId()] = temp_cost
                f_n = temp_cost + neighbor.getHeuristic()
                heapq.heappush(to_explore, (f_n, id(neighbor), neighbor))
                from_vertex[neighbor.getId()] = current_vertex.getId()

    return None, None, visited_order


def reconstruct_path(from_vertex, goal):
    path = []
    current = goal.getId()
    while current is not None:
        path.append(current)
        current = from_vertex.get(current)
    return path[::-1]


def heuristic(vertex, goal_vertex):
    vertex.heuristic_val = abs(vertex.getX() - goal_vertex.getX()) + abs(vertex.getY() - goal_vertex.getY())


def heuristic_goal(vertex):
    vertex.heuristic_val = 0
    return vertex


def main(graph):
    labels = {
        "A": "University Mall",
        "B": "Mcdonalds",
        "C": "Pericos",
        "D": "Bloemen Hall",
        "E": "W.H. Taft Residence",
        "F": "EGI Taft",
        "G": "Castro Street",
        "H": "Agno Food Court",
        "I": "One Archer's",
        "J1": "Br. Andrew Gonzales Hall",
        "J2": "Enrique Razon Sports Center",
        "K": "Green Mall",
        "L": "Green Court",
        "M": "Sherwood",
        "N": "Jollibee",
        "O": "Dagong St.",
        "P": "Burgundy",
        "Q": "Estrada St.",
        "R": "D' Student's Place",
        "S": "Leon Guinto St.",
        "T": "P.Ocampo St.",
        "U": "Fidel A. Reyes St."
    }

    print("\nAvailable Locations: ")
    for key, value in labels.items():
        print(f"{key} - {value}")
    print()

    start_id = input("Enter start: ").strip().upper()
    goal_id = input("Enter goal: ").strip().upper()

    start = graph.getVertex(start_id)
    goal = graph.getVertex(goal_id)

    if not start or not goal:
        print(f"Error: Start '{start_id}' or goal '{goal_id}' not found.")
        return

    heuristic_goal(goal)
    for v_id in graph.getVertices():
        heuristic(graph.getVertex(v_id), goal)

    path, total_cost, _ = A_Star(graph, start, goal)

    if path:
        print("Path found:", " -> ".join(path))
        print(f"Total Cost: {total_cost}")
        return path
    else:
        print("No path found")
        return None
