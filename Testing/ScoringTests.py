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

        score.score_full_house([1, 1, 1, 2, 2], [1, 2])
        self.assertEqual(score.scores[8], 25)
        score.reset()

        score.score_full_house([2, 2, 3, 3, 3], [2, 3])
        self.assertEqual(score.scores[8], 25)
        score.reset()

        score.score_full_house([4, 4, 4, 4, 5], [4, 5])
        self.assertEqual(score.scores[8], 0)
        score.reset()

        score.score_full_house([3, 4, 4, 4, 4], [3, 4])
        self.assertEqual(score.scores[8], 0)

    def test_score_straights(self):
        score = Scoring()

        score.score_straights([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
        self.assertEqual(score.scores[9:10], [30, 40])

        score.score_straights([], [])
        self.assertEqual(score.scores[9:10], [])

        score.score_straights([], [])
        self.assertEqual(score.scores[9:10], [])

    def test_score_multiple_same_kind(self):
        pass

    def test_score_chance(self):
        pass

if __name__ == '__main__':
    unittest.main()