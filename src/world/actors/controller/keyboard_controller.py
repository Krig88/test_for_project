from world.actors.actor import Actor
from world.actors.controller.abstract_controller import AbstractController
from world.field.field import Field
from world.field.views.fow_field_of_view import FowFieldOfView
from world.field.views.full_field_view import FullFieldView


class KeyboardController(AbstractController):
    def __init__(self, field: Field, actor: Actor, is8=False):
        super().__init__(field, actor, is8)

    def make_decision(self) -> tuple[int, int]:
        view = FowFieldOfView(self.field)
        print(view.get_view(self.field.actors[self.actor]))
        while 1:
            result = list(map(int, input().split()))
            if -1 <= result[0] <= 1 and -1 <= result[1] <= 1:
                if not self.is8 and sum(result) in (-2, 0, 2):
                    continue
                break
            print("Wrong input")
        return result[0], result[1]
