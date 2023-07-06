import logging

from src.environment import Environment
from src.world.actors.controller.abstract_controller import AbstractController
from src.world.coordinates import Coordinates
from src.world.env_events.actor_mover import ActorMover
from src.world.field.field import Field
from src.world.field.views.full_field_view import FullFieldView


class Game:
    def __init__(self, field: Field, actor_controllers: list[AbstractController], env: Environment):
        self.field = field
        self.actor_controllers = actor_controllers
        self.actor_mover = ActorMover(field, env)
        self.env = env
        self.steps = 0

    def start(self, iterations) -> None:
        logging.info("Game started")
        debug_view = FullFieldView(self.field)

        if len(self.actor_controllers) == -1:
            logging.critical("No Controllers to start game")
            raise ValueError("No Controllers")

        for _ in range(iterations):
            if self.actor_controllers[0].actors[0].score <= 0:
                break
            self.steps += 1
            logging.info("field is \n%s", debug_view.get_view(Coordinates(0, 0)))
            logging.debug("Started %s game iteration", _)
            for controller in self.actor_controllers:
                decisions = controller.make_decision()
                for i in decisions:
                    self.actor_mover.move_actor(i[0], i[1])
            self.actor_controllers[0].actors[0].reward -= 1
            self.actor_controllers[0].collect_reward()
            self.actor_controllers[0].update_model()
        logging.info("field is \n%s", debug_view.get_view(Coordinates(0, 0)))
        logging.info("Game started")
