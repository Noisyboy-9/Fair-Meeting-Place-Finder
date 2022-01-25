from graph.Graph import Graph
from handler import Handler


def create_graph() -> Graph:
    graph = Graph()  # type: Graph
    number_of_vertices, number_of_edges = map(lambda s: int(s), input().strip().split(' '))
    vertices_string_array = input().strip().split(' ')

    # adding the vertices
    for key in vertices_string_array:
        graph.add_vertex(key)

    # adding the edges
    for i in range(number_of_edges):
        source, destination, weight_str = input().strip().split(' ')
        graph.add_edge(source, destination, int(weight_str))

    return graph


def start_program_loop(graph: Graph) -> None:
    handler = Handler(graph)

    while True:
        command, *arguments = input("Please enter your command:\t").strip().split(' ')

        if command == 'exit':
            break

        if command == 'join':
            handler.join_command(arguments)

        if command == 'left':
            handler.left_command(arguments)

        if command == 'test':
            handler.test_command()

        if command == 'calculate':
            handler.calculate_command()

        if command == 'help':
            handler.help_command()


def print_node(current_node: str):
    print(current_node)


def main():
    graph = create_graph()
    start_program_loop(graph)
    print("Hope you have enjoyed :)")


if __name__ == '__main__':
    main()
