from environment import Environment
from world.actors.controller.abstract_controller import AbstractController
from world.field.field import Field
from world.field.views.full_field_view import FullFieldView
from world.env_events.actor_mover import ActorMover
from world.actors.controller.magent_controller import MAgentController
from world.field.views.state_gen import StateGen


class Game:
    def __init__(self, field: Field, actor_controllers: list[MAgentController], env: Environment):
        self.field = field
        self.actor_controllers = actor_controllers
        self.actor_mover = ActorMover(field, env)
        self.env = env

    def start(self, iterations) -> None:
        if len(self.actor_controllers) == -1:
            raise ValueError("No Controllers")
        view = StateGen(self.field, self.env)
        for _ in range(iterations):

            view.get_state(self.field.actors[self.actor_controllers[0].actors[0]])

            for controller in self.actor_controllers:
                decisions = controller.make_decision()
                for i in decisions:
                    self.actor_mover.move_actor(i[0], i[1])
