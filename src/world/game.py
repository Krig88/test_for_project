import logging

import for_logging.agents_statistic as a_stat
from src.configurations.game_config import GameConfig as Conf
from src.environment import Environment
from src.world.actors.controller.abstract_controller import AbstractController
from src.world.actors.controller.agent_controller import AgentController
from src.world.actors.player import Player
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
            # player = self.actor_controllers[0].actors[0]
            # player_pos = self.field.actors[player]
            logging.info("field is \n%s", debug_view.get_view(Coordinates(0, 0)))
            logging.debug("Started %s game iteration", j)
            for controller in self.actor_controllers:
                decisions = controller.make_decision()
                for i in decisions:
                    self.actor_mover.move_actor(i[0], i[1])
            # TODO rework skip move reward (fixed)
            # if player_pos == self.field.actors[player]:
            #     player.reward += Conf.skip_reward
            #     a_stat.agents_statistic_folder[player].skips += 1

            for controller in self.agents_controllers:
                controller.collect_reward()
                if j % Conf.steps_to_update_model == 0:
                    controller.update_model()

        logging.info("field is \n%s", debug_view.get_view(Coordinates(0, 0)))

    def clear_dead(self) -> int:
        num_of_actors = 0
        for controller in self.agents_controllers:
            for actor in controller.actors:
                if actor.score <= 0:  # Что?
                    self.field.actors.pop(actor)
                    controller.actors.remove(actor)
                    continue
                num_of_actors += 1
        return num_of_actors
