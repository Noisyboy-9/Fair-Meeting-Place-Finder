import math

from graph.Vertex import Vertex


def unvisited_node_with_smallest_distance(not_visited_node: list, distances: dict) -> Vertex:
    result = not_visited_node[0]  # type: str
    result_distance = distances[result]  # type: int

    for node in not_visited_node:
        if distances[node] < result_distance:
            result = node
            result_distance = distances[node]

    return result


class Graph:
    def __init__(self) -> None:
        self.__vertices = []  # type: list[Vertex]
        self.__adjacency_list = {}
        self.__starting_points = []  # type: list[Vertex]

    @property
    def starting_points(self):
        return self.__starting_points

    @property
    def adjacency_list(self):
        return self.__adjacency_list

    @property
    def vertices(self):
        return self.__vertices

    def add_vertex(self, vertex: Vertex):
        if vertex in self.__vertices:
            raise ValueError(f"Can't add duplicate vertex key. Vertex with key = {vertex.key} already exist")

        self.__vertices.append(vertex)
        self.__adjacency_list[vertex] = []

    def add_edge(self, vertex1: Vertex, vertex2: Vertex, weight: int):
        self.__adjacency_list[vertex1].append([vertex2, weight])
        self.__adjacency_list[vertex2].append([vertex1, weight])

    def add_starting_point(self, start: Vertex):
        if start in self.__starting_points:
            raise ValueError(f"The starting point, {start.key}, is duplicate can't!")

        if start not in self.__vertices:
            raise ValueError(
                f"starting point must be a vertex on the graph, the graph doesn't have vertex equal to {start.key}"
            )

        self.__starting_points.append(start)
        start.dijkstra_result = self.dijkstra(start)

    def remove_starting_point(self, remove_target: Vertex):
        if remove_target not in self.__starting_points:
            raise ValueError(f"starting point: {remove_target.key} isn't declared before!")
        self.__starting_points.remove(remove_target)
        remove_target.dijkstra_result = {}

    def dfs_print(self, visited: set, current_node: Vertex):
        if current_node not in visited:
            if len(visited) == len(self.__vertices) - 1:
                # last node to visit put a line break at the end
                print(current_node.key)
            else:
                print(current_node.key, end = " ")

            visited.add(current_node)
            for edge in self.__adjacency_list[current_node]:
                neighbor_vertex, weight = edge[0], edge[1]
                self.dfs_print(visited, neighbor_vertex)

    def dijkstra(self, start: Vertex) -> dict:
        distances = {vertex: math.inf for vertex in self.__vertices}
        distances[start] = 0

        not_visited_nodes = [i for i in self.__vertices]

        while len(not_visited_nodes) != 0:
            current_vertex = unvisited_node_with_smallest_distance(not_visited_nodes, distances)
            not_visited_nodes.remove(current_vertex)

            for edge in self.__adjacency_list[current_vertex]:
                neighbor, weight = edge[0], edge[1]
                current_distance = distances[current_vertex] + weight

                if current_distance < distances[neighbor]:
                    distances[neighbor] = current_distance

        return distances

    def calculate_fair_score(self, calculation_target, dijkstra_results):
        score = 0

        if len(self.__starting_points) == 2:
            first, second = self.__starting_points

            first_distance = dijkstra_results[first][calculation_target]
            last_distance = dijkstra_results[second][calculation_target]

            return math.fabs(first_distance - last_distance)

        for point in self.__starting_points:
            score += dijkstra_results[point][calculation_target]

        return score / len(self.__starting_points)
