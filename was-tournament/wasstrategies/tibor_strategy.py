from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D

class Tibor(Player):
    """A modified Tit-for-Tat player that switches to permanent defection
    if the opponent defects more than 3 times.
    
    The player starts by cooperating, then:
    1. Copies the opponent's last move (Tit-for-Tat behavior)
    2. If opponent has defected more than 3 times total, always defects
    """

    name = "Tibor"
    classifier = {
        "memory_depth": float('inf'),  # Infinite memory needed to count defections
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
            
        # Count total defections by opponent
        defection_count = sum(1 for action in opponent.history if action == D)
        
        # If opponent defected more than 3 times, always defect
        if defection_count > 3:
            return D
            
        # Otherwise, copy opponent's last move (Tit-for-Tat)
        return opponent.history[-1]