from world.field.field import Field
from world.actors.actor import Actor
from world.actors.controller.abstract_controller import AbstractController
from world.coordinates import Coordinates


class MAgentController:

    def __init__(self, controller_type, field: Field, actors: list[Actor]):
        self.controllers = [controller_type(field, i) for i in actors]
        self.field = field
        self.actors = actors

    def make_decision(self) -> list[tuple[Actor, Coordinates]]:
        decisions = []
        for controller in self.controllers:
            decision = controller.make_decision()
            decisions.append((controller.actor, decision))

        return decisions
