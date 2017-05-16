# Reserved by Phil
# has a method that returns different scores with different choices of scoring options



class Scoring:
    """Provides methods to return possible scoring options"""



    def score_options(dice_list):


        scores = {'ones':0, 'twos':0, 'threes':0, 'fours':0, 'fives':0, 'sixes':0, 'threekind':0, 'fourkind':0,\
                  'fullhouse':0, 'smstraight':0, 'lgstraight':0, 'yahtzee':0, 'chance':0}

        #ones
        count = 0
        for count in (0,6)
            if dice_list[count] == 1:
                scores['ones'] = scores['ones'] + 1
            count = count + 1
        #twos
        count = 0
        for count in (0,6)
            if dice_list[count] == 2:
                scores['twoes'] = scores['twoes'] + 2
            count = count + 1
        #threes
        count = 0
        scores[count-1] = dice_list[0] + dice_list[1] + dice_list[2] + dice_list[3] + dice-list[4]