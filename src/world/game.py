import logging

from environment import Environment
from world.actors.controller.abstract_controller import AbstractController
from world.coordinates import Coordinates
from world.field.field import Field
from world.field.views.full_field_view import FullFieldView
from world.env_events.actor_mover import ActorMover
from world.actors.controller.magent_controller import MAgentController
from world.field.views.state_gen import StateGen


class Game:
    def __init__(self, field: Field, actor_controllers: list[AbstractController], env: Environment):
        self.field = field
        self.actor_controllers = actor_controllers
        self.actor_mover = ActorMover(field, env)
        self.env = env

    def start(self, iterations) -> None:
        logging.info("Game started")
        debug_view = FullFieldView(self.field)

        if len(self.actor_controllers) == -1:
            logging.critical("No Controllers to start game")
            raise ValueError("No Controllers")
        for _ in range(iterations):
            logging.info("field is \n%s", debug_view.get_view(Coordinates(0, 0)))
            logging.debug("Started %s game iteration", _)
            for controller in self.actor_controllers:
                decisions = controller.make_decision()
                for i in decisions:
                    self.actor_mover.move_actor(i[0], i[1])
        logging.info("field is \n%s", debug_view.get_view(Coordinates(0, 0)))
        logging.info("Game started")
