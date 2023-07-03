
from world.actors.actor import Actor
from world.actors.controller.abstract_controller import AbstractController
from world.field.field import Field
from world.coordinates import Coordinates
from environment import Environment
from  world.field.views.state_gen import StateGen


class AgentController(AbstractController):

    def __init__(self, field: Field, actors: list[Actor], env: Environment = None):
        super().__init__(field, actors)
        self.state_view = StateGen(field, env)

    def make_decision(self, state: list = None) -> list[tuple[Actor, Coordinates]]:
        raise NotImplementedError

    def collect_reward(self, reward: int) -> None:
        raise NotImplementedError
