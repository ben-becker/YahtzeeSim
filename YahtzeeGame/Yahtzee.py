# Reserved by Ben

from random import randint
from YahtzeeGame import Scoring

class Yahtzee:
    """Provides methods to run a yahtzee game"""
    score = 0
    score_value_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    score_filled_list = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    game_over = False

    def run_hand(self, player):
        dice_list = [0, 0, 0, 0, 0]

        # randomly sets dice list
        for i in range(len(dice_list)):
            dice_list[i] = randint(1, 2, 3, 4, 5, 6)

        # goes through three rounds
        for round_num in range(1, 4):
            # get input from player on which to keep
            global score_value_list
            keep_array = player.get_decisions(dice_list, score_value_list, 0, round_num)

            # roll again non needed ones
            for dice_index in range(len(keep_array)):
                if not keep_array[dice_index]:
                    dice_list[dice_index] = randint(1, 2, 3, 4, 5, 6)

        return dice_list

    def run_game(self, player):
        while not game_over:
            # end dice = run hand
            dice_list = self.run_hand(player)

            # save score from dice
            score_list = Scoring.score_options(dice_list)

            # if all the scores are filled, game is over
            if all(score_filled_list for score_filled_list in score_filled_list):
                game_over = True

        # returns the sum of all the scores
        return sum(score_value_list for score_value_list in score_value_list)