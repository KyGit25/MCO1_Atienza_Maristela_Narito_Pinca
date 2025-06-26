from pythonds.graphs import Graph, Vertex
import networkx as nx
import matplotlib.pyplot as plt
import BFS
import A


def undirected_connect(graph, v1, v2, weight=0):
    graph.addEdge(v1.getId(), v2.getId(), weight)
    graph.addEdge(v2.getId(), v1.getId(), weight)
    v1.addNeighbor(v2, weight)
    v2.addNeighbor(v1, weight)


def initialize_graph():
    graph = Graph()

    A = Vertex("A", 21, 3)
    B = Vertex("B", 20, 3)
    C = Vertex("C", 19, 2)
    D = Vertex("D", 12, 1)
    E = Vertex("E", 11, 4)
    F = Vertex("F", 10, 4)
    G = Vertex("G", 8, 4)
    H = Vertex("H", 8, 0)
    I = Vertex("I", 7, 4)
    J1 = Vertex("J1", 5, 3)
    J2 = Vertex("J2", 5, 0)
    K = Vertex("K", 4, 3)
    L = Vertex("L", 6, 1)
    M = Vertex("M", 4, 6)
    N = Vertex("N", 6, 6)
    O = Vertex("O", 11, 6)
    P = Vertex("P", 14, 6)
    Q = Vertex("Q", 15, 6)
    R = Vertex("R", 18, 6)
    S = Vertex("S", 14, 7)
    T = Vertex("T", 22, 6)
    U = Vertex("U", 2, 2)

    vertices = [A, B, C, D, E, F, G, H, I, J1, J2, K, L, M, N, O, P, Q, R, S, T, U]
    for v in vertices:
        graph.addVertex(v.getId(), v.getX(), v.getY(), v.getHeuristic())

    connections = [
        (U, K, 20), (U, J2, 30), (J2, J1, 45), (K, J1, 10), (K, M, 400),
        (M, N, 25), (J1, I, 10), (J2, L, 35), (J1, L, 20), (L, I, 20),
        (I, G, 15), (L, H, 20), (I, H, 25), (G, H, 30), (G, F, 20),
        (H, F, 55), (N, O, 120), (F, O, 145), (F, E, 10), (O, E, 130),
        (O, S, 40), (O, P, 30), (E, P, 145), (E, D, 30), (S, P, 60),
        (D, P, 165), (P, Q, 10), (S, Q, 50), (D, C, 90), (Q, R, 25),
        (R, C, 180), (R, B, 140), (C, B, 40), (R, T, 20), (B, T, 120),
        (B, A, 15), (A, T, 135)
    ]

    for v1, v2, w in connections:
        undirected_connect(graph, v1, v2, w)

    return graph


def convert_to_nx_graph(graph):
    nx_graph = nx.Graph()
    pos = {}

    for v_id in graph.getVertices():
        vertex = graph.getVertex(v_id)
        nx_graph.add_node(v_id, heuristic=vertex.getHeuristic())
        pos[v_id] = (vertex.getX(), vertex.getY())

        for neighbor in vertex.getConnections():
            nx_graph.add_edge(v_id, neighbor.getId(), weight=vertex.getWeight(neighbor))

    return nx_graph, pos


def visualize_graph(graph):
    nx_graph, pos = convert_to_nx_graph(graph)
    plt.figure(figsize=(16, 8))
    plt.title("Graph Visualization")
    nx.draw(nx_graph, pos, with_labels=True, node_color="lightblue", edge_color="grey", node_size=500, font_size=10)
    plt.show()


def visualize_path(graph, path, title):
    nx_graph, pos = convert_to_nx_graph(graph)
    plt.figure(figsize=(16, 8))
    plt.title(f"{title} Visualization")

    for i in range(len(path) - 1):
        nx.draw(nx_graph, pos, with_labels=True, node_color="yellow", edge_color="grey", node_size=500, font_size=10)
        nx.draw_networkx_edges(nx_graph, pos, edgelist=[(path[i], path[i + 1])], edge_color="darkorange", width=2)
        nx.draw_networkx_nodes(nx_graph, pos, nodelist=[path[i]], node_color="darkorange", node_size=700)
        plt.pause(0.5)

    nx.draw_networkx_nodes(nx_graph, pos, nodelist=[path[-1]], node_color="red", node_size=700)
    plt.show()


def run_algorithm(graph):
    while True:
        print("\nSelect algorithm to run:")
        print("1. Breadth-First Search (BFS)")
        print("2. A* Search")
        print("3. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            path = BFS.main(graph)
            if path:
                visualize_path(graph, path, "BFS")
        elif choice == '2':
            path = A.main(graph)
            if path:
                visualize_path(graph, path, "A* Search")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")


def main():
    graph = initialize_graph()

    while True:
        print("\nMenu:")
        print("1. Run Algorithm")
        print("2. Visualize Graph")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            run_algorithm(graph)
        elif choice == '2':
            visualize_graph(graph)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()
