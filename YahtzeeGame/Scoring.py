# has a method that returns different scores with different choices of scoring options


class Scoring:
    """Provides methods to return possible scoring options"""

    def __init__(self):
        # order: ones, twos, threes, fours, fives, sixes, three kind, four kin
        # full house, small straight, large straight, yahtzee, chance
        self.scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def reset(self):
        self.__init__()

    def score_one_through_sixes(self, dice_sorted):
        # goes from 1's to 6's
        for number in range(1, 7):
            # goes through all the dice
            for dice_index in range(0, 5):
                # adds to respective score if the number matches the category
                if dice_sorted[dice_index] == number:
                    self.scores[number - 1] += number

    def score_full_house(self, dice_sorted, dice_no_repeat):
        # checks to make sure exactly two different numbers appear in all the five dice
        if len(dice_no_repeat) == 2:
            # check to avoid dice set in the form ABBBB or AAAAB by comparing first two and last two dice
            # works because the dice list is sorted
            if dice_sorted[0] == dice_sorted[1] and dice_sorted[4] == dice_sorted[3]:
                self.scores[8] = 25

    def score_straights(self, dice_no_repeat):
        # checks for large straight in ascending order no repeat list
        if dice_no_repeat == [1, 2, 3, 4, 5]:
            self.scores[10] = 40
            self.scores[9] = 30

        # checks for small straight in ascending order no repeat list
        if dice_no_repeat == [1, 2, 3, 4] or dice_no_repeat == [2, 3, 4, 5]:
            self.scores[9] = 30

    def score_multiple_same_kind(self, dice_sorted, dice_no_repeat):
        # check for five of a kind (only one dice number shows up)
        if len(dice_no_repeat) == 1:
            # save Yahtzee score
            self.scores[12] = 50
            # also save three/four of a kind score
            self.scores[7] = self.scores[6] = sum(dice_sorted)

        # check for four of a kind
        # by checking that two dice numbers show up and that the end pairs don't match
        # to eliminate sets in the form AABBB or AAABB
        elif len(dice_no_repeat) == 2 and dice_sorted[0] != dice_sorted[1] and dice_sorted[4] != dice_sorted[3]:
            # add up score of all dice and also save to three of a kind
            self.scores[7] = self.scores[6] = sum(dice_sorted)

        # check for three of a kind
        # first check that three dice numbers show up (if full house, already stored)
        elif len(dice_no_repeat) == 3:
            # loop to check that in sorted list there are three numbers equal somewhere
            # not the form AABBC or ABBCC or AABCC
            for num in range(0, 3):
                if dice_sorted[num] == dice_sorted[num + 1] == dice_sorted[num + 2]:
                    # add up the score of all the dice
                    self.scores[6] = sum(dice_sorted)
                    break

    def score_chance(self, dice):
        self.scores[12] = sum(dice)

    def score_options(self, dice_list):
        # sorts dice into ascending order
        dice_sorted = sorted(dice_list)

        # deletes duplicate dice
        dice_no_repeat = list(set(dice_sorted))

        # scores all options
        self.score_one_through_sixes(dice_sorted)
        self.score_full_house(dice_sorted, dice_no_repeat)
        self.score_straights(dice_no_repeat)
        self.score_multiple_same_kind(dice_sorted, dice_no_repeat)
        self.score_chance(dice_sorted)
