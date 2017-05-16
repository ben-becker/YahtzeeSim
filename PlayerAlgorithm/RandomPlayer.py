# Unreserved
# RandomPlayer makes random decisions

from random import randint
from PlayerAlgorithm import Player


class RandomPlayer(Player):

    def get_decision(self, dice_list, scorecard, num_hands, num_rolls):
        """Method to return random decisions"""
        decision_list = []
        for i in range(0, 6):
            if randint(0, 1) == 0:
                decision_list.append(True)
            else:
                decision_list.append(False)
        return decision_list
