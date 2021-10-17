from random import shuffle

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(suit, value))

    def __repr__(self):
        return "Cards remaining in deck: ()".format(len(self.cards))

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt")
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)


deck = Deck()
deck.shuffle()
while True:
    input()
    print(len(deck), "cards in the deck")
    print(deck.deal())