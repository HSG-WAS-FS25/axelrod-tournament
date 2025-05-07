from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D


class Christoph(Player):
    """
    Pavlov Strategy.
    """

    name = "Christoph"
    classifier = {
        "memory_depth": 10,
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def strategy(self, opponent: Player) -> Action:
        if not self.history:
            return C
        if self.history[-1] == opponent.history[-1]:
            return self.history[-1]
        else:
            return D if self.history[-1] == C else C
