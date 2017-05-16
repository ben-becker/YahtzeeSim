# Reserved by Phil
# has a method that returns different scores with different choices of scoring options



class Scoring:
    """Provides methods to return possible scoring options"""



    def score_options(dice_list):


        scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # writes sum of ones-sixes
        for count in (0,6):
            if dice_list[count] == count + 1:
                scores[count] = scores[count] + 1

        #writes chance
        scores[] = dice_list[0] + dice_list[1] + dice_list[2] + dice_list[3] + dice-list[4]