import tensorflow as tf
from tensorflow.python.keras.optimizer_v2.adam import Adam
import tensorflow.python.keras.optimizers
import tensorflow_probability as tfp
from src.world.actors.controller.actor_critic.networks import ActorCriticNetwork
import numpy as np

class Agent:
    def __init__(self, alpha=0.01, gamma=0.99, n_actions=4):
        self.gamma = gamma
        self.n_actions = n_actions
        self.action = None

        self.actor_critic = ActorCriticNetwork(n_actions=n_actions)
        optimizer = Adam(learning_rate=alpha)
        self.actor_critic.compile(optimizer=optimizer)

    def choose_action(self, observation):
        state = tf.convert_to_tensor([observation])
        print(state)
        p, probs = self.actor_critic(state)
        print(probs)
        action_probabilities = tfp.distributions.Categorical(probs=probs)
        print(action_probabilities)
        action = action_probabilities.sample()
        #log_prob = action_probabilities.log_prob(action)
        self.action = action
        print(action)
        print("----------------------------")
        return np.argmax(action.numpy()[0])

    def save_models(self):
        print('... saving models ...')
        self.actor_critic.save_weights(self.actor_critic.checkpoint_file)

    def load_models(self):
        print('... loading models ...')
        self.actor_critic.load_weights(self.actor_critic.checkpoint_file)

    def learn(self, state, reward, state_, done=False):
        state = tf.convert_to_tensor([state], dtype=tf.float32)
        state_ = tf.convert_to_tensor([state_], dtype=tf.float32)
        reward = tf.convert_to_tensor(reward, dtype=tf.float32)  # not fed to NN
        with tf.GradientTape(persistent=True) as tape:
            state_value, probs = self.actor_critic(state)
            state_value_, _ = self.actor_critic(state_)
            state_value = tf.squeeze(state_value)
            state_value_ = tf.squeeze(state_value_)

            action_probs = tfp.distributions.Categorical(probs=probs)
            log_prob = action_probs.log_prob(self.action)

            delta = reward + self.gamma * state_value_ * (1 - int(done)) - state_value
            actor_loss = -log_prob * delta
            critic_loss = delta ** 2
            total_loss = actor_loss + critic_loss

        gradient = tape.gradient(total_loss, self.actor_critic.trainable_variables)
        self.actor_critic.optimizer.apply_gradients(zip(
            gradient, self.actor_critic.trainable_variables))
