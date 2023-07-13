import numpy as np
import tensorflow as tf
from keras import layers

from src.world.actors.controller.actor_critic.actor_critic import Agent
from src.environment import Environment
from src.world.actors.actor import Actor
from src.world.actors.controller.abstract_controller import AbstractController
from src.world.actors.player import Player
from src.world.coordinates import Coordinates
from src.world.field.field import Field
from src.world.field.views.state_gen import StateGen


class AgentController(AbstractController):
    def __init__(self, field: Field, actors: list[Actor], env: Environment = None):
        super().__init__(field, actors)
        self.state_view = StateGen(field, env)
        self.list_of_actions = env.directions
        self.num_actions = len(self.list_of_actions)
        self.agent = Agent()
        #self.agent = Agent(n_actions=self.num_actions)
        self.last_state = None
        self.last_reward = None

    def collect_reward(self):
        # unhardcoded
        for actor in self.actors:
            if not isinstance(actor, Player):
                continue
            actor.score += actor.reward
            self.last_reward = actor.reward
            actor.reward = 0

    def make_decision(self, state: list = None) -> list[tuple[Actor, Coordinates]]:
        self.last_state = self.state_view.get_state(self.actors[0])
        decision = self.agent.choose_action(self.last_state)
        return [(self.actors[0], self.list_of_actions[decision])]
    # new_state = self.state_view.get_state(self.actors[0])

    def update_model(self):
        self.collect_reward()
        if self.last_state is None or self.last_state is None or self.last_reward is None:
            return

        new_state = self.state_view.get_state(self.actors[0])
        self.agent.learn(self.last_state, self.last_reward, new_state)





