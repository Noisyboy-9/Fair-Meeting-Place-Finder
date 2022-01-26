class Vertex:
    def __init__(self, key: str) -> None:
        super().__init__()
        self.__key = key

    @property
    def key(self):
        return self.__key

    def __eq__(self, target: object) -> bool:
        return isinstance(target, Vertex) and self.__key == target.__key

    def __hash__(self) -> int:
        return hash(self.__key)

    def __ne__(self, o: object) -> bool:
        return not self.__eq__(o)
