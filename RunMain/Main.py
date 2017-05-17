from YahtzeeGame.Yahtzee import Yahtzee
from PlayerAlgorithm.RandomPlayer import RandomPlayer

game = Yahtzee()
player = RandomPlayer()

score_sum = 0

for i in range(0, 100000):
    game = Yahtzee()
    score = game.run_game(player)
    score_sum += score

print(score_sum/100000)
