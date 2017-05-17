import unittest
from YahtzeeGame.Scoring import Scoring


class ScoringTests(unittest.TestCase):
    def test_score_ones_through_sixes(self):
        score = Scoring()

        score.score_one_through_sixes([1, 2, 3, 4, 5])
        self.assertEqual(score.scores[0:6], [1, 2, 3, 4, 5, 0])
        score.reset()

        score.score_one_through_sixes([3, 3, 3, 3, 3])
        self.assertEqual(score.scores[0:6], [0, 0, 15, 0, 0, 0])
        score.reset()

        score.score_one_through_sixes([1, 2, 2, 2, 2])
        self.assertEqual(score.scores[0:6], [1, 8, 0, 0, 0, 0])
        score.reset()

        score.score_one_through_sixes([3, 3, 4, 4, 4])
        self.assertEqual(score.scores[0:6], [0, 0, 6, 12, 0, 0])
        score.reset()

        score.score_one_through_sixes([5, 5, 5, 5, 6])
        self.assertEqual(score.scores[0:6], [0, 0, 0, 0, 20, 6])

    def test_score_full_house(self):
        score = Scoring()

        score.score_full_house([], [])
        self.assertEqual(score.scores[8] == 25)
        score.reset()

    def test_score_straights(self):
        pass

    def test_score_multiple_same_kind(self):
        pass

    def test_score_chance(self):
        pass

if __name__ == '__main__':
    unittest.main()