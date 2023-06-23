from src.world.actors import Actor


class Cell:
    def __init__(self,
                 passable: bool = True,
                 actor: Actor = None,
                 position: tuple[int, int] = (0, 0),
                 neighbours: dict = None) -> None:
        raise NotImplementedError()
