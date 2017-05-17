from YahtzeeGame.Yahtzee import Yahtzee
from PlayerAlgorithm.RandomPlayer import RandomPlayer

game = Yahtzee()
player = RandomPlayer()
print(game.run_game(player))

# should work