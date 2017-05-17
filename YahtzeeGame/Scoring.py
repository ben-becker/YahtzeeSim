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
            # goes through all the dice and counts the number
            for dice_index in range(0, 5):
                if dice[dice_index] == number:
                    self.scores[number-1] += number

    def score_full_house(self, dice, dice_no_repeat):
        if len(dice_no_repeat) == 2:
            if dice[0] == dice[1] and dice[4] == dice[3]:
                self.scores[8] = 25
            else:
                self.scores[8] = 0

    def score_straights(self, dice, dice_no_repeat):
        for number in range(1, 7):
            # check if dice actually form large straight (increase by 1 for all dice)
            if dice[number - 1] == dice[number - 1] + 1:
                self.scores[10] = 40
                self.scores[9] = 30
            # check if dice actually form small straight
            elif len(dice_no_repeat) == 4 and dice_no_repeat[number - 1] == dice_no_repeat[number - 1] + 1:
                self.scores[9] = 30
                self.scores[10] = 0
            else:
                self.scores[10] = 0
                self.scores[9] = 0
                break

    def score_multiple_same_kind(self, dice, dice_no_repeat):
        # check for five of a kind
        if len(dice_no_repeat) == 1:
            self.scores[12] = 50
            self.scores[7] = self.scores[6] = sum(dice for dice in dice)

        # check for four of a kind
        elif len(dice_no_repeat) == 2 and dice[0] != dice[1] and dice[4] != dice[3]:
            self.scores[7] = self.scores[6] = sum(dice for dice in dice)

        # check for three of a kind
        elif len(dice_no_repeat) == 3:
            self.scores[12] = self.scores[7] = 0

            for num in range(0, 3):
                if dice[num] == dice[num + 1] == dice[num + 2]:
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
