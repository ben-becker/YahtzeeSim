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

        score.score_straights([1, 2, 3, 4, 5])
        self.assertEqual(score.scores[9:11], [30, 40])
        score.reset()

        score.score_straights([2, 3, 4, 5, 6])
        self.assertEqual(score.scores[9:11], [30, 40])
        score.reset()

        score.score_straights([1, 2, 3, 4])
        self.assertEqual(score.scores[9:11], [30, 0])
        score.reset()

        score.score_straights([2, 3, 4, 5])
        self.assertEqual(score.scores[9:11], [30, 0])
        score.reset()

        score.score_straights([3, 4, 5, 6])
        self.assertEqual(score.scores[9:11], [30, 0])
        score.reset()

        score.score_straights([1, 2, 3])
        self.assertEqual(score.scores[9:11], [0, 0])
        score.reset()

        score.score_straights([1, 4, 6])
        self.assertEqual(score.scores[9:11], [0, 0])
        score.reset()

        score.score_straights([1, 2, 3, 4, 6])
        self.assertEqual(score.scores[9:11], [30, 0])
        score.reset()

        score.score_straights([1, 3, 4, 5, 6])
        self.assertEqual(score.scores[9:11], [30, 0])

    def test_score_multiple_same_kind(self):
        score = Scoring()

        score.score_multiple_same_kind([1, 1, 1, 1, 1], [1])
        score_list = score.scores[6:8] + [score.scores[12]]
        self.assertEquals(score_list, [5, 5, 50])
        score.reset()

        score.score_multiple_same_kind([1, 1, 1, 1, 2], [1, 2])
        score_list = score.scores[6:8] + [score.scores[12]]
        self.assertEquals(score_list, [6, 6, 0])
        score.reset()

        score.score_multiple_same_kind([1, 2, 2, 2, 2], [1, 2])
        score_list = score.scores[6:8] + [score.scores[12]]
        self.assertEquals(score_list, [9, 9, 0])
        score.reset()

        score.score_multiple_same_kind([1, 1, 2, 2, 2], [1, 2])
        score_list = score.scores[6:8] + [score.scores[12]]
        self.assertEquals(score_list, [8, 0, 0])
        score.reset()

        score.score_multiple_same_kind([1, 1, 1, 2, 2], [1, 2])
        score_list = score.scores[6:8] + [score.scores[12]]
        self.assertEquals(score_list, [7, 0, 0])
        score.reset()

        score.score_multiple_same_kind([1, 1, 1, 2, 3], [1, 2, 3])
        score_list = score.scores[6:8] + [score.scores[12]]
        self.assertEquals(score_list, [8, 0, 0])
        score.reset()

        score.score_multiple_same_kind([1, 1, 2, 2, 3], [1, 2, 3])
        score_list = score.scores[6:8] + [score.scores[12]]
        self.assertEquals(score_list, [0, 0, 0])
        score.reset()

        score.score_multiple_same_kind([1, 2, 2, 3, 3], [1, 2, 3])
        score_list = score.scores[6:8] + [score.scores[12]]
        self.assertEquals(score_list, [0, 0, 0])
        score.reset()

    def test_score_chance(self):
        pass

if __name__ == '__main__':
    unittest.main()
