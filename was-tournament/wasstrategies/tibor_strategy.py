from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D

class Tibor(Player):
    """A modified Tit-for-Tat player that switches to permanent defection
    if the opponent defects more than 2 times in a row.
    
    The player starts by cooperating, then:
    1. Copies the opponent's last move (Tit-for-Tat behavior)
    2. If opponent has defected more than 2 times in a row, defects
    3. Counter resets when opponent cooperates
    """

    name = "Tibor"
    classifier = {
        "memory_depth": 3,  # We only need to remember last 3 moves
        "stochastic": False,
        "long_run_time": False,
        "inspects_source": False,
        "manipulates_source": False,
        "manipulates_state": False,
    }

    def strategy(self, opponent: Player) -> Action:
        # For first move, cooperate
        if not opponent.history:
            return C
            
        # Count consecutive defections by looking at recent history in reverse
        consecutive_defections = 0
        for action in reversed(opponent.history):
            if action == D:
                consecutive_defections += 1
            else:
                break
        
        # If opponent defected more than 2 times in a row, defect
        if consecutive_defections > 2:
            return D
            
        # Otherwise, copy opponent's last move (Tit-for-Tat)
        return opponent.history[-1]