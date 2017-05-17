from random import randint
from YahtzeeGame.Scoring import Scoring


class Yahtzee:
    """Provides methods to run a yahtzee game"""
    score = 0
    score_value_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    score_filled_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self):
        self.score = 0
        self.score_value_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.score_filled_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def run_hand(self, player):
        dice_list = [0, 0, 0, 0, 0]

        # randomly sets dice list
        for i in range(len(dice_list)):
            dice_list[i] = randint(1, 6)

        # goes through three rounds
        for round_num in range(1, 4):
            # get input from player on which to keep
            keep_array = player.get_decisions()

            # roll again non needed ones
            for dice_index in range(len(keep_array)):
                if not keep_array[dice_index]:
                    dice_list[dice_index] = randint(1, 2, 3, 4, 5, 6)

        return dice_list

    def pick_score(self, potential_list):
        potential_sorted_descending = list(reversed(sorted(potential_list)))
        original_indices = [b[0] for b in reversed(sorted(enumerate(potential_list), key=lambda j:j[1]))]

        for i in range(len(potential_sorted_descending)):
            index = original_indices[i]
            if self.score_filled_list[index] == 0:
                self.score_value_list[index] = potential_sorted_descending[i]
                self.score_filled_list[index] = 1
                break

    def run_game(self, player):
        game_over = False
        while not game_over:
            # end dice = run hand
            dice_list = self.run_hand(player)

            # save score from dice
            score_machine = Scoring()
            score_machine.score_options(dice_list)

            #print(self.score_filled_list)

            self.pick_score(score_machine.scores)

            # if all the scores are filled, game is over
            if sum(self.score_filled_list) == 13:
                game_over = True

        # returns the sum of all the scores
        return sum(self.score_value_list)
