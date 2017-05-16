# Reserved by Phil
# has a method that returns different scores with different choices of scoring options


class Scoring:
    """Provides methods to return possible scoring options"""

    def score_options(self, dice_list):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # sorts dice into ascending order
        dice = sorted(dice_list)
        # deletes duplicate dice
        set_dice = set(dice)

        # writes scoring for ones-sixes
        for number in range(1, 7):
            for dice_index in range(0, 6):
                if dice[dice_index] == number:
                    scores[number-1] += number

        # writes scoring for full house
            # check if dice actually form full house (two-three matching)
            if len(set_dice) == 2:
                if dice[0] == dice[1] and dice[4] == dice[3]:
                    scores[8] = 25
                else:
                    scores[8] = 0

        # writes scoring for large and small straight
        for number in range(1, 7):
            # check if dice actually form large straight (increase by 1 for all dice)
            if dice[number - 1] == dice[number - 1] + 1:
                scores[10] = 40
                scores[9] = 30
            # check if dice actually form small straight
            elif len(set_dice) == 4 and set_dice[number - 1] == set_dice[number - 1] + 1:
                scores[9] = 30
                scores[10] = 0
            else:
                scores[10] = 0
                scores[9] = 0
                break

        # writes scoring for three/four/five kind
        # check if all dice are equal
        if len(set_dice) == 1:
            scores[12] = 50
            scores[7] = sum(dice for dice in dice)
            scores[6] = sum(dice for dice in dice)
        # check for four of a kind
        elif len(set_dice) == 2 and dice[0] != dice[1] and dice[4] != dice[3]:
                scores[7] = sum(dice for dice in dice)
                scores[6] = sum(dice for dice in dice)
        # check for three of a kind
        elif len(set_dice) == 3:
            scores[12] = 0
            scores[7] = 0
            for num in range(0, 3):
                if dice[num] == dice[num + 1] == dice[num + 2]:
                    scores[6] = sum(dice for dice in dice)
                else:
                    continue
        else:
            scores[12] = 0
            scores[7] = 0
            scores[6] = 0

        # writes scoring for chance
        scores[12] = sum(dice for dice in dice)
