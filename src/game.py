import logging

import for_logging.agents_statistic as a_stat
from src.configuration.game_config import GameConfig as Conf
from src.environment import Environment
from src.world.actors.controller.abstract_controller import AbstractController
from src.world.actors.controller.agent_controller import AgentController
from src.world.actors.player import Player
from src.world.coordinates import Coordinates
from src.world.field.field import Field
from src.world.field.views.full_field_view import FullFieldView


class Game:
    def __init__(self, field: Field, actor_controllers: list[AbstractController], env: Environment):
        self.field = field
        self.actor_controllers = actor_controllers
        self.env = env
        self.steps = 0
        self.agents_controllers: list[AgentController] = [
            i for i in actor_controllers if isinstance(i, AgentController)
        ]

    def start(self, iterations) -> None:
        logging.info("Game started")
        debug_view = FullFieldView(self.field)

        if len(self.actor_controllers) == -1:
            logging.critical("No Controllers to start game")
            raise ValueError("No Controllers")

        for j in range(iterations):

            if Conf.mortality:
                if not self.clear_dead():
                    break

            for actor in self.field.actors:
                if isinstance(actor, Player):
                    a_stat.agents_statistic_folder[actor].steps += 1

            self.steps += 1
            logging.info("field is \n%s", debug_view.get_view(Coordinates(0, 0)))
            logging.debug("Started %s game iteration", j)
            for controller in self.actor_controllers:
                decisions = controller.make_decision()
                for actor, coordinates in decisions:
                    self.env.move_actor(actor, coordinates)

            for controller in self.agents_controllers:
                if j % Conf.steps_to_update_model == 0:
                    controller.update_model()
        logging.info("field is \n%s", debug_view.get_view(Coordinates(0, 0)))

    def clear_dead(self) -> int:
        num_of_actors = 0
        for controller in self.agents_controllers:
            for actor in controller.actors:
                if not isinstance(actor, Player):
                    continue
                if actor.score <= 0:
                    self.field.actors.pop(actor)
                    controller.actors.remove(actor)
                    continue
                num_of_actors += 1
        return num_of_actors
