from dataclasses import dataclass
from src.world.actors.player import Player


@dataclass
class AgentStatistic:
    number: int = 0
    cats: int = 0
    dogs: int = 0
    skips: int = 0
    steps: int = 0
    score: int = 0


agents_statistic_folder: dict[Player: AgentStatistic] = {}


def add_agent_to_folder(agent: Player) -> None:
    agents_statistic_folder[agent] = AgentStatistic()


def get_statistic(agent: Player) -> AgentStatistic:
    return agents_statistic_folder.get(agent)


def update_score():
    for actor in agents_statistic_folder:
        agents_statistic_folder.get(actor).score = actor.score


