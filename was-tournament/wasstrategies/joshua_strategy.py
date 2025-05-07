from axelrod.action import Action
from axelrod import Player

C, D = Action.C, Action.D

class Joshua(Player):
    """
    Starts by cooperating.
    If opponent defects in round 1, still cooperates in round 2 (grace).
    But if opponent defects again in round 2 → defects in round 3 (punishment).
    From round 4 onwards, forgives if the opponent cooperates twice in a row.
    """

    name = "Joshua"
    classifier = {
        "memory_depth": 2,
        "stochastic": False,
        "makes_use_of": set(),
    }

    def strategy(self, opponent) -> Action:
        round_num = len(self.history)

        # Round 1: Always cooperate
        if round_num == 0:
            return C

        # Round 2: Always cooperate (grace)
        if round_num == 1:
            return C

        # Round 3: If opponent defected again in round 2, defect. Otherwise cooperate
        if round_num == 2:
            return D if opponent.history[1] == D else C

        # Round 4 and beyond: Forgive if opponent cooperated last 2 rounds
        if opponent.history[-1] == C and opponent.history[-2] == C:
            return C

        # Default: defect
        return D