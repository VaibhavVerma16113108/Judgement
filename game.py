from player import Player
from typing import List
from scoreboard import Scoreboard
from deck import Deck
import json


class Game:
    def __init__(self, config):
        self.multiplier = config["multiplier"]
        self.num_players = len(config["players"])
        self.num_rounds = config["num_rounds"]
        self.curr_round = 1
        self.players = self.initialise_players(config)
        self.scoreboard = Scoreboard(self)

    def initialise_players(self, config) -> List[Player]:
        """
        Generate a list of players who will play the game.
        """
        players = []
        for i in range(1, self.num_players + 1):
            name = config["players"][i-1]
            player = Player(name)
            players.append(player)
        return players

    def start_round(self):
        self.running_sum_bid = 0
        deck = Deck()
        for player in self.players:
            player.initialise_hand(deck, self.num_rounds - self.curr_round)
            print(player.name)
            player.see_hand()
        for player in self.players:
            print(f"{player.name} - please enter your bid: ")
            bid = int(input())
            player.make_bid(bid, game)

    def play_round(self):
        num_turns = self.num_rounds - self.curr_round + 1
        # TODO: keep a dataframe (players X turns) containing each player's moves in
        # every turn

    def end_round(self):
        self.curr_round += 1
        self.update_scores()
        # rotate the players list by 1
        self.players.insert(0, self.players.pop())

    def update_scores(self):
        self.scoreboard.update_scores(self)

    def play(self):
        while self.curr_round <= self.num_rounds:
            self.start_round()
            self.play_round()
            self.end_round()


if __name__ == "__main__":
    with open("./config.json") as f:
        config = json.load(f)
    game = Game(config)
    game.start_round()
    game.scoreboard.show()
