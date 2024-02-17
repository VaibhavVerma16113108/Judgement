from deck import Deck
from utils import retry


class Player:
    def __init__(self, name: str):
        self.name = name

    def see_hand(self):
        for card in self.hand:
            card.show()

    def see_bid(self):
        print(f"{self.name} - {self.bid}")

    # round-specific methods
    def initialise_hand(self, deck: Deck, round_number: int):
        """
        At the start of every round, call this method to assign a hand to the player
        """
        self.hand = []
        for _ in range(round_number):
            card = deck.draw_card()
            self.hand.append(card)

    @retry(tries=3)
    def make_bid(self, bid: int, game):
        """
        Inputs:
            bid: int - the bid that the player wants to make.
            running_sum_bid: int - the sum of the bids that other players have made till now.
            round_number: int - the number of the round in progress (ranging from [1...n])
        """
        # TODO: instead of passing running_sum_bid and round_number, it might be better to pass the Game object
        sum_not_allowed = game.num_rounds - game.curr_round + 1
        assert bid <= sum_not_allowed, "Cannot bid more than possible number of hands."
        assert bid != sum_not_allowed - \
            game.running_sum_bid, f"Cannot make a bid such that sum of all bids = {round_number}."
        self.bid = bid

    def play_card(self, card: str):
        pass
        # if input string matches the str representation of the card, we play it
        # and remove it from the hand


if __name__ == "__main__":
    player = Player("Vaibhav")
    deck = Deck()
    player.initialise_hand(deck, 9)
    player.see_hand()
