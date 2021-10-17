class Card():

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show_card(self):
        print(str(self.value) + " of " + str(self.suit))

class Deck():

    card_list = []

    def __init__(self):
        self.construct_deck()
        self._playing_pile = []
        self._discard_pile = []

    def construct_deck(self):
        for s in ['Clubs', 'Diamonds', 'Hearts', 'Spades']:
            for v in ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']:
                self.card_list.append(Card(v, s))

    def show_deck(self):
        for card in self.card_list:
            card.show_card()

    def show_playing_pile(self):
        for card in self._playing_pile:
            card.show_card()

    def show_discard_pile(self):
        for card in self._discard_pile:
            card.show_card()

    def shuffle_deck(self):
        self.shuffled_cards = random.shuffle(self.card_list)

    def draw_card_from_deck(self):
        self._draw_from_deck = self.card_list.pop()
        return self._draw_from_deck

    def return_card_to_deck(self):
        self._return_to_deck = self.card_list.append(self._draw_from_deck)
        return self._return_to_deck

    def put_card_in_playing_pile(self):
        self._put_in_playing_pile = self._playing_pile.append(self._draw_from_deck)
        return self._put_in_playing_pile

    def put_card_in_discard_pile(self):
        self._put_in_discard_pile = self._discard_pile.append(self._draw_from_deck)
        return self._put_in_discard_pile

class Player(Deck):

    def __init__(self, name):
        self.name = name
        self._players_hand = []

    def player_draws_card_from_deck(self, deck):
        self._players_hand.append(deck.draw_card_from_deck())

    def player_returns_card_from_hand_to_deck(self, deck):
        self.card_list.append(self._players_hand.pop())

    def player_returns_card_from_playing_pile_to_deck(self, deck):
        self.card_list.append(self._playing_pile.pop())

    def player_returns_card_from_discard_pile_to_deck(self, deck):
        self.card_list.append(self._discard_pile.pop())

    def show_players_hand(self):
        for card in self._players_hand:
            card.show_card()



