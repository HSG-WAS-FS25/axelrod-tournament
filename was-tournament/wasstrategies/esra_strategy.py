from axelrod.action import Action, actions_to_str
from axelrod.player import Player
from axelrod.strategy_transformers import (
    FinalTransformer,
    TrackHistoryTransformer,
)

C, D = Action.C, Action.D


class Esra(Player):
    """
    It deflects in the first round and then 
    cooperates with the opponent. If the opponent cooperates, it continues to cooperate. If the opponent defects, it will defect in the round after the next one.
    """

    name = "Esra"
    classifier = {
        "memory_depth": 1,
        'stochastic': False,
        'inspects_source': False,
        'manipulates_source': False,
        'manipulates_state': False
    }

    def strategy(self, opponent: Player) -> Action:
        """This is the actual strategy"""
        # First move
        if len(opponent.history) <2:
            return D
        # React to the opponent's last move
        if opponent.history[-2] == D:
            return D
        elif opponent.history[-2] == C:
            return C
        else:
            return C