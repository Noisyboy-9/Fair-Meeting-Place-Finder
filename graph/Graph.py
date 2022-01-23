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
