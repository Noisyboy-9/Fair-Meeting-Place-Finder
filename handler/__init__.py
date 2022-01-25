from graph.Graph import Graph


class Handler:
    def __init__(self, graph: Graph) -> None:
        self.__graph = graph  # type: Graph

    def join_command(self, arguments):
        self.__graph.add_starting_point(arguments[0])

    def left_command(self, arguments):
        self.__graph.remove_starting_point(arguments[0])

    def test_command(self):
        self.__graph.dfs_print(set(), self.__graph.vertices[0])

    def calculate_command(self):
        if len(self.__graph.starting_points) == 0:
            print("No starting points can't do any calculations!")
            return

        if len(self.__graph.starting_points) == len(self.__graph.vertices):
            print("All the vertices has been declared as starting point! Justice is a dream ! :)")
            return

        dijkstra_results = {
            starting_point: self.__graph.dijkstra(starting_point) for starting_point in self.__graph.starting_points
        }
        possible_places = list(set(self.__graph.vertices).difference(self.__graph.starting_points))
        scores = {}

        for place in possible_places:
            scores[place] = self.__graph.calculate_fair_score(place, dijkstra_results)

        min_value = min(scores.values())
        print([key for key, value in scores.items() if value == min_value])

    def help_command(self):
        print("Commands:")
        print("1. join")
        print("2. left")
        print("3. test")
        print("4. calculate")



