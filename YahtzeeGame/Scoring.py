# Reserved by Phil
# has a method that returns different scores with different choices of scoring options


class Scoring:
    """Provides methods to return possible scoring options"""

    # order: ones, twos, threes, fours, fives, sixes, three kind, four kin
    # full house, small straight, large straight, yahtzee, chance
    scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def score_one_through_sixes(self, dice):
        # goes from 1's to 6's
        for number in range(1, 7):
            # goes through all the dice and checks if the number corresponds to the category i.e.(ones, twos, etc.)
            for dice_index in range(0, 5):
                # if the number matches the category it is added to the the score for that category
                if dice[dice_index] == number:
                    self.scores[number-1] += number

    # parameters for following methods:
    # dice = sorted list of 5 dice in ascending order
    # dice_no_repeat = dice list but with all repeated numbers removed

    def score_full_house(self, dice, dice_no_repeat):
        # checks to make sure exactly two different numbers appear in all the five dice
        if len(dice_no_repeat) == 2:
            # check to avoid dice set in the form ABBBB or AAAAB by comparing first two and last two dice
            if dice[0] == dice[1] and dice[4] == dice[3]:
                self.scores[8] = 25
                # also save to three of a kind score
                self.scores[6] = sum(dice for dice in dice)
            else:
                self.scores[8] = 0

    def score_straights(self, dice, dice_no_repeat):
        for number in range(1, 7):
            # check if dice actually form large straight (increase by 1 for all dice)
            if dice[number - 1] == dice[number - 1] + 1:
                # save lg straight score
                self.scores[10] = 40
                # also save sm straight score
                self.scores[9] = 30
            # check if dice actually form small straight
            # by checking if there are exactly four different dice numbers and that they increase by one
            elif len(dice_no_repeat) == 4 and dice_no_repeat[number - 1] == dice_no_repeat[number - 1] + 1:
                self.scores[9] = 30
                self.scores[10] = 0
            else:
                self.scores[10] = 0
                self.scores[9] = 0
                break

    def score_multiple_same_kind(self, dice, dice_no_repeat):
        # check for five of a kind (only one dice number shows up)
        if len(dice_no_repeat) == 1:
            # save Yahtzee score
            self.scores[12] = 50
            # also save three/four of a kind score
            self.scores[7] = self.scores[6] = sum(dice for dice in dice)

        # check for four of a kind
        # by checking that two dice numbers show up and that the end pairs don't match
        # to eliminate sets in the form AABBB or AAABB
        elif len(dice_no_repeat) == 2 and dice[0] != dice[1] and dice[4] != dice[3]:
            # add up score of all dice and also save to three of a kind
            self.scores[7] = self.scores[6] = sum(dice for dice in dice)

        # check for three of a kind
        # first check that three dice numbers show up (if full house, already stored)
        elif len(dice_no_repeat) == 3:
            # if there are three different dice numbers, four and five of a kind are zero
            self.scores[12] = self.scores[7] = 0
            # loop to check that in sorted list there are three numbers equal somewhere
            # not the form AABBC or ABBCC or AABCC
            for num in range(0, 3):
                if dice[num] == dice[num + 1] == dice[num + 2]:
                    # add up the score of all the dice
                    self.scores[6] = sum(dice for dice in dice)
                else:
                    continue
        else:
            self.scores[12] = self.scores[7] = self.scores[6] = 0

    def score_chance(self, dice):
        # sums all dice
        self.scores[12] = sum(dice for dice in dice)

    def score_options(self, dice_list):
        # sorts dice into ascending order
        dice = sorted(dice_list)

        # deletes duplicate dice
        dice_no_repeat = list(set(dice))

        # scores all options
        self.score_one_through_sixes(dice)
        self.score_full_house(dice, dice_no_repeat)
        self.score_straights(dice, dice_no_repeat)
        self.score_multiple_same_kind(dice, dice_no_repeat)
        self.score_chance(dice)
