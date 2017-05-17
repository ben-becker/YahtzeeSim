import unittest
from YahtzeeGame.Scoring import Scoring

class ScoringTests(unittest.TestCase):

    def test_score_ones_through_sixes(self):
        score = Scoring()

        score.score_one_through_sixes([1, 2, 3, 4, 5])
        self.assertEqual(score.scores[0:6], [1, 2, 3, 4, 5, 0])

    def test_score_full_house(self):
        pass

    def test_score_straights(self):
        pass

    def test_score_multiple_same_kind(self):
        pass

    def test_score_chance(self):
        pass

if __name__ == '__main__':
    unittest.main()