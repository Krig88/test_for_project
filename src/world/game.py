import logging

from src.environment import Environment
from src.world.actors.controller.abstract_controller import AbstractController
from src.world.coordinates import Coordinates
from src.world.env_events.actor_mover import ActorMover
from src.world.field.field import Field
from src.world.field.views.full_field_view import FullFieldView
from src.world.actors.player import Player
from src.configurations.game_config import GameConfig as Conf
from src.world.actors.controller.agent_controller import AgentController



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

        for j in range(iterations):
            if Conf.mortality:
                if not self.clear_dead():
                    break

            self.steps += 1
            player = self.actor_controllers[0].actors[0]
            player_pos = self.field.actors[player]
            logging.info("field is \n%s", debug_view.get_view(Coordinates(0, 0)))
            logging.debug("Started %s game iteration", j)
            for controller in self.actor_controllers:
                decisions = controller.make_decision()
                for i in decisions:
                    self.actor_mover.move_actor(i[0], i[1])

            if player_pos == self.field.actors[player]:
                player.reward += Conf.skip_reward
            self.actor_controllers[0].collect_reward()
            if j % Conf.steps_to_update_model == 0:
                self.actor_controllers[0].update_model()

        logging.info("field is \n%s", debug_view.get_view(Coordinates(0, 0)))

    def clear_dead(self) -> int:
        num_of_actors = 0
        for controller in self.actor_controllers:
            if isinstance(controller, AgentController):
                for actor in controller.actors:
                    if actor.score <= 0:
                        self.field.actors.pop(actor)
                        controller.actors.remove(actor)
                        continue
                    num_of_actors += 1
        return num_of_actors
