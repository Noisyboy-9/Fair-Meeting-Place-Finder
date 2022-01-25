import math


def unvisited_node_with_smallest_distance(not_visited_node: list, distances: dict) -> str:
    result = not_visited_node[0]  # type: str
    result_distance = distances[result]  # type: int

    for node in not_visited_node:
        if distances[node] < result_distance:
            result = node
            result_distance = distances[node]

    return result


class Graph:
    def __init__(self) -> None:
        self.__vertices = []
        self.__adjacency_list = {}
        self.__starting_points = []

    def add_vertex(self, vertex_key: str):
        if vertex_key in self.__vertices:
            raise ValueError(f"Can't add duplicate vertex key. Vertex with key = {vertex_key} already exist")

        self.__vertices.append(vertex_key)
        self.__adjacency_list[vertex_key] = []

    def add_edge(self, vertex1: str, vertex2: str, weight: int):
        self.__adjacency_list[vertex1].append([vertex2, weight])
        self.__adjacency_list[vertex2].append([vertex1, weight])

    def add_starting_point(self, starting_point: str):
        if starting_point in self.__starting_points:
            raise ValueError(f"The starting point, {starting_point}, is duplicate can't!")

        if starting_point not in self.__vertices:
            raise ValueError(
                f"starting point must be a vertex on the graph, the graph doesn't have vertex equal to {starting_point}"
            )

        self.__starting_points.append(starting_point)

    def remove_starting_point(self, starting_point: str):
        if starting_point not in self.__starting_points:
            raise ValueError(f"starting point: {starting_point} isn't declared before!")

        self.__starting_points.remove(starting_point)

    @property
    def vertices(self):
        return self.__vertices

    def dfs_print(self, visited: set, current_node: str):
        if current_node not in visited:
            print()
            visited.add(current_node)
            for edge in self.__adjacency_list[current_node]:
                neighbor_vertex, weight = edge[0], edge[1]
                self.dfs_print(visited, neighbor_vertex)

    def dijkstra(self, start: str) -> dict:
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

    def handle_calculate_command(self):
        if len(self.__starting_points) == 0:
            return "No starting points can't do any calculations!"

        dijkstra_results = {starting_point: self.dijkstra(starting_point) for starting_point in self.__starting_points}
        possible_places = list(set(self.__vertices).difference(self.__starting_points))
        scores = {}

        for place in possible_places:
            scores[place] = self.calculate_fair_score(place, dijkstra_results)

        min_value = min(scores.values())
        return [key for key, value in scores.items() if value == min_value]

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
