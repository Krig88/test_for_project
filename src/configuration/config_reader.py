import json

from for_logging import agents_statistic
import src.configuration.rules as rules
from src.game import Game
from src.world.actors.actor import Actor
from src.world.actors.cat import Cat
from src.world.actors.controller.agent_controller import AgentController
from src.world.actors.controller.catdog import CatDog
from src.world.actors.controller.keyboard_controller import KeyboardController
from src.world.actors.controller.random_contoller import RandomController
from src.world.actors.dog import Dog
from src.world.actors.player import Player
from src.world.coordinates import Coordinates
from src.world.field.field import Field
from src.environment import Environment, Connectedness, tf
from src.world.world_configurator import WorldConfigurator

controller_type = {"CatDog": CatDog, "KeyboardController": KeyboardController,
                   "RandomController": RandomController, "AgentController": AgentController}
actor_type = {"Player": Player, "Cat": Cat, "Dog": Dog}


def read_controllers(param, wc, env):
    controllers = []
    for controller in param:
        name = list(controller.keys())[0]
        actors = read_actors(controller[name], wc)
        controllers.append(controller_type[name](wc.field, actors, env))
    return controllers


def read_actors(param, wc) -> list[Actor]:
    result = []
    to_place = []
    for i, actor in enumerate(param):
        name = list(actor.keys())[0]
        actor = actor_type[name]()
        cords = param[i][name]
        if isinstance(actor, Player):
            agents_statistic.add_agent_to_folder(actor)
        result.append(actor)
        to_place.append(
            (actor, Coordinates(*cords))
        )
    wc.apply_rules(
        (rules.place_actors,),
        (to_place, )
    )
    return result


def read_field(param) -> WorldConfigurator:
    wc = WorldConfigurator(
        Coordinates(*param['size'])
    )
    wc.apply_rules(
        (rules.place_walls,),
        tuple([(Coordinates(*coordinates), ) for coordinates in param['walls']['coordinates']])
    )
    return wc


def read_env(param, field):
    con = Connectedness.FOUR_CONNECTEDNESS if param['Connectedness'] == 4 else \
        Connectedness.EIGHT_CONNECTEDNESS
    return Environment(field, con, tf)  # unhardcode tf


def configurate(path: str = None) -> tuple[Field, Environment, Game, WorldConfigurator]:
    with open(path, "r") as read_file:
        config = json.load(read_file)

    wc = read_field(config['Field'])
    env = read_env(config['Environment'], wc.field)
    controllers = read_controllers(config['controllers'], wc, env)

    field = wc.field
    g = Game(field, controllers, env)
    if field is None or env is None or g is None:
        raise Exception('Cannot read config')
    return field, env, g, wc
