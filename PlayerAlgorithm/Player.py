# Unreserved
# Parent class for all players


class Player:
    """Common class for all players"""

    def __init__(self):
        pass

    @staticmethod
    def get_decisions():
        # returns instructions to keep all dice
        return [True, True, True, True, True]
