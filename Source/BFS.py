from collections import deque

def BFS(graph, start, goal):
    to_explore = deque([start])
    visited = set()
    from_vertex = {start.getId(): None}
    visited_order = []

    while to_explore:
        current = to_explore.popleft()
        current_id = current.getId()
        visited_order.append(current)

        if current_id == goal.getId():
            path = reconstruct_path(from_vertex, goal)
            cost = calculate_path_cost(graph, path)
            return path, cost, visited_order

        visited.add(current_id)

        for neighbor in current.getConnections():
            neighbor_id = neighbor.getId()
            if neighbor_id not in visited and neighbor_id not in from_vertex:
                to_explore.append(neighbor)
                from_vertex[neighbor_id] = current_id

    return None, None, visited_order


def calculate_path_cost(graph, path):
    total_cost = 0
    for i in range(len(path) - 1):
        current = graph.getVertex(path[i])
        next_node = graph.getVertex(path[i+1])
        total_cost += current.getWeight(next_node)
    return total_cost


def reconstruct_path(from_vertex, goal):
    path = []
    current = goal.getId()
    while current is not None:
        path.append(current)
        current = from_vertex.get(current)
    return path[::-1]


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

    path, total_cost, _ = BFS(graph, start, goal)

    if path:
        print("Path found:", " -> ".join(path))
        print(f"Total Cost: {total_cost}")
        return path
    else:
        print("No path found")
        return None
