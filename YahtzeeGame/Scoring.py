# Reserved by Phil
# has a method that returns different scores with different choices of scoring options


class Scoring:
    """Provides methods to return possible scoring options"""

    def score_options(dice_list):
        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # writes scoring for ones-sixes
        for number in range(1, 7):
            for dice_index in range(0, 6):
                if dice_list[dice_index] == number:
                    scores[number-1] += number

        # need scoring for small/large straight


        # need scoring for three/four/five kind

        # writes scoring for chance
        scores[12] = sum(dice_list for dice_list in dice_list)
