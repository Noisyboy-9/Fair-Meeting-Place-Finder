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
