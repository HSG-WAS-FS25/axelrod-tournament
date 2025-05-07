from axelrod.action import Action, actions_to_str
from axelrod.player import Player


class Constantin(Player):
    name = "Constantin"
    resentment_memory = 10
    classifier = {
        "memory_depth": 10,
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def strategy(self, opponent: Player) -> Action:
        # Calculate resentment_time based on the last 3 actions of the opponent
        resentment_time = len([d for d in opponent.history[-self.resentment_memory:] if d == Action.D])

        if opponent.history and (
                opponent.history[-1] == Action.D or opponent.history[-resentment_time:] == [Action.D]
        ):
            return Action.D
        return Action.C