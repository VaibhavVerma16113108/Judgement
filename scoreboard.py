import pandas as pd


class Scoreboard:
    def __init__(self, game):
        self.scores = pd.DataFrame(index=range(
            len(game.players)), columns=range(game.num_rounds + 1)).fillna(0)
        self.set_index(game)
        self.set_columns(game)
        self.multiplier = game.multiplier

    def set_index(self, game):
        player_names = [player.name for player in game.players]
        self.scores.index = player_names

    def set_columns(self, game):
        cols = [i for i in range(1, game.num_rounds + 1)] + ["total"]
        self.scores.columns = cols

    def update_scores(self, game):
        for player in game.players:
            if player.has_won_round():
                scores.loc[player.name][game.curr_round] = self.multiplier * player.bid

    def show(self):
        print(self.scores)
