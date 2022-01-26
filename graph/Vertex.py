class Vertex:
    def __init__(self, key: str) -> None:
        super().__init__()
        self.__key = key

    def __eq__(self, target: object) -> bool:
        return isinstance(target, Vertex) and self.__key == target.__key
    