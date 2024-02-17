import random
from card import Card


class Deck:
    def __init__(self):
        """
        Initialising a Deck object creates a shuffled
        deck of 52 cards.
        """
        self.cards = []
        self.build()
        self.shuffle()

    def build(self):
        suits = ["spades", "diamonds", "clubs", "hearts"]
        vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        for suit in suits:
            for val in vals:
                card = Card(suit, val)
                self.cards.append(card)

    def show(self):
        """
        Prints out the entire deck.
        """
        for card in self.cards:
            card.show()

    def shuffle(self):
        # this is called the Fisher-Yates shuffle
        for i in range(len(self.cards) - 1, -1, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        """
        Returns one card from the deck.
        """
        return self.cards.pop()
