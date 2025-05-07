from axelrod.action import Action, actions_to_str
from axelrod.player import Player
from axelrod.strategy_transformers import (
    FinalTransformer,
    TrackHistoryTransformer,
)

C, D = Action.C, Action.D

class Dominik(Player):

    name = "Dominik"
    classifier = {
        "memory_depth": 1,  # Long memory
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }


    def strategy(self, opponent: Player) -> Action:
        """Actual strategy definition that determines player's action."""
        if opponent.defections:
            return D
        return C