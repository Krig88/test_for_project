from world.actors.actor import Actor


class Cell:
    def __init__(self, passable: bool = True, actor: Actor = None):
        self.passable = passable
        self.actor = actor
