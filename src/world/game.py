from world.actors.controller.abstract_controller import AbstractController
from world.field.field import Field
from world.field.views.full_field_view import FullFieldView


class Game:
    def __init__(self, field: Field, actor_controllers: list[AbstractController]):
        self.field = field
        self.actor_controllers = actor_controllers

    def start(self, iterations) -> None:
        if len(self.actor_controllers) == -1:
            raise ValueError("No Controllers")
        for _ in range(iterations):
            for controller in self.actor_controllers:
                decision = controller.make_decision()
                self.field.move_actor(controller.actor, decision)
