class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print("{} of {}".format(self.val, self.suit))

    def __eq__(self, card):
        return self.suit == card.suit and self.val == card.val

    def __gt__(self, card):
        if self.suit == card.suit:
            return self.val > card.val
        else:
            return True

    def __lt__(self, card):
        if self.suit == card.suit:
            return self.val < card.val
        else:
            return False

    def compare(self, card):
        if self == card:
            return 0
        elif self > card:
            return 1
        return -1
