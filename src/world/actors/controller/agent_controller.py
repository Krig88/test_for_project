import numpy as np
import tensorflow as tf
from keras import layers

from src.environment import Environment
from src.world.actors.actor import Actor
from src.world.actors.controller.abstract_controller import AbstractController
from src.world.coordinates import Coordinates
from src.world.field.field import Field
from src.world.field.views.state_gen import StateGen


class AgentController(AbstractController):
    def __init__(self, field: Field, actors: list[Actor], env: Environment = None):
        super().__init__(field, actors)
        self.state_view = StateGen(field, env)
        self.list_of_actions = [Coordinates(1, 0), Coordinates(0, 1), Coordinates(0, -1), Coordinates(-1, 0)]
        num_actions = 4  # [[1,0], [0,1], [0,-1], [-1,0]]
        # num_state = np.matrix(4, 3)  # self.state_view.size  # TODO: Размерность пространства состояний

        # Создание модели Actor-Critic
        inputs = layers.Input(shape=(12,))
        common = layers.Dense(128, activation='relu')(inputs)
        action = layers.Dense(num_actions, activation='softmax')(common)
        critic = layers.Dense(1)(common)

        self.model = tf.keras.Model(inputs=inputs, outputs=[action, critic])
        self.optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
        self.huber_loss = tf.keras.losses.Huber()

        self.last_state = None
        self.last_action = None
        self.last_reward = None

    def collect_reward(self):
        self.last_reward = self.actors[0].reward
        self.actors[0].score += self.actors[0].reward
        self.actors[0].reward = 0

    def make_decision(self, state: list = None) -> list[tuple[Actor, Coordinates]]:
        q = self.state_view.get_state(self.actors[0])
        s = []
        for i in q:
            s += i
        state = tf.convert_to_tensor(
            tf.reshape(
                s, 12
            )
        )
        state = tf.expand_dims(state, 0)

        # state = np.reshape(state, 12)
        action_probabilities, _ = self.model(state)

        action = np.random.choice(4, p=np.squeeze(action_probabilities))

        self.last_state = state
        self.last_action = action

        # TODO: Преобразовать индекс действия обратно в координаты
        return [(self.actors[0], self.list_of_actions[action])]

    # new_state = self.state_view.get_state(self.actors[0])

    def update_model(self):
        if self.last_state is None or self.last_reward is None or self.last_action is None:
            return
        q = self.state_view.get_state(self.actors[0])
        s = []
        for i in q:
            s += i
        new_state = tf.convert_to_tensor(
            tf.reshape(
                s, 12
            )
        )
        new_state = tf.expand_dims(new_state, 0)

        _, next_critic_value = self.model(new_state)

        with tf.GradientTape() as tape:
            action_probabilities, critic_value = self.model(self.last_state)

            td_target = self.last_reward + 0.99 * next_critic_value
            delta = td_target - critic_value

            actions_one_hot = tf.one_hot([self.last_action], 4)
            action_probabilities_for_selected_actions = tf.reduce_sum(action_probabilities * actions_one_hot)

            actor_loss = -tf.math.log(action_probabilities_for_selected_actions) * delta
            critic_loss = self.huber_loss(tf.expand_dims(critic_value, 0), tf.expand_dims(td_target, 0))
            total_loss = actor_loss + critic_loss

        grads = tape.gradient(total_loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))
