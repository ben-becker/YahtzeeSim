# Unreserved
# RandomPlayer makes random decisions

from random import randint
from PlayerAlgorithm import Player


class RandomPlayer(Player.Player):

    def __init__(self):
        pass

    def get_decision(self):
        """Method to return random decisions"""
        decision_list = []
        for i in range(0, 6):
            if randint(0, 1) == 0:
                decision_list.append(True)
            else:
                decision_list.append(False)
        return decision_list
