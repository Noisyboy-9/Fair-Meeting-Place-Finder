from graph.Graph import Graph


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
    while True:
        command, *arguments = input().strip().split(' ')

        if command == 'exit':
            break

        if command == 'join':
            pass

        if command == 'left':
            pass

        if command == 'test':
            graph.handle_test()
            

def main():
    graph = create_graph()
    start_program_loop(graph)
    print("Hope you have enjoyed :)")


if __name__ == '__main__':
    main()
