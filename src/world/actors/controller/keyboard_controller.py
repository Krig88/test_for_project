from world.actors.actor import Actor
from world.actors.controller.abstract_controller import AbstractController
from world.field.field import Field
from world.field.views.fow_field_of_view import FowFieldOfView
from world.field.views.full_field_view import FullFieldView
from world.coordinates import Coordinates
from environment import Environment


class KeyboardController(AbstractController):
    def __init__(self, field: Field, actors: list[Actor], is8=False, env: Environment = None):
        super().__init__(field, actors, is8)

    def make_decision(self, state: list = None) -> list[tuple[Actor, Coordinates]]:
        # view = FowFieldOfView(self.field)
        view = FullFieldView(self.field)
        results = []

        print(view.get_view())

        for actor in self.actors:
            while 1:
                pre_result = list(map(int, input().split()))
                result = Coordinates(pre_result[0], pre_result[1])
                if -1 <= result.x <= 1 and -1 <= result.y <= 1:
                    if not self.is8 and sum(pre_result) in (-2, 0, 2):
                        continue
                    break
                print("Wrong input")
            results.append((actor, result))
        return results
