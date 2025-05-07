from axelrod.action import Action, actions_to_str
from axelrod.player import Player
from axelrod.strategy_transformers import (
    FinalTransformer,
    TrackHistoryTransformer,
)

C, D = Action.C, Action.D

class Jano(Player):
    """A player starts by cooperating and then defects only after two defects by
    opponent.

    Submitted to Axelrod's second tournament by John Maynard Smith; it came in
    24th in that tournament.

    Names:

    - Tit for two Tats: [Axelrod1984]_
    - Slow tit for two tats: Original name by Ranjini Das
    - JMaynardSmith: [Axelrod1980b]_
    """

    name = "Jano"
    classifier = {
        "memory_depth": 2, 
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }


    def strategy(self, opponent: Player) -> Action:
        return D if len(self.history) < 10 else C
