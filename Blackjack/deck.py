from card import Card
import random

class Deck:
    '''
    The deck has a list of cards
    '''
    def __init__(self):
        self.cards = []

    '''
    Makes a standard deck of 52 cards
    '''
    def build_deck(self) -> None:
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks_vals = {
            "Ace" : (1, 11),
            "2" : 2,
            "3" : 3,
            "4" : 4,
            "5" : 5,
            "6" : 6,
            "7" : 7,
            "8" : 8,
            "9" : 9,
            "10" : 10,
            "King" : 10,
            "Queen" : 10,
            "Jack" : 10
        }

        for s in suits:
            for r, v in ranks_vals.items():
                self.cards.append(Card(s, r, v))

    '''
    Shuffles the deck of cards
    '''
    def shuffle(self) -> None:
        random.shuffle(self.cards)

    '''
    Deals a card to a participant
    '''
    def deal_card(self) -> Card:
        return self.cards.pop()

    '''
    Returns the number of cards remaining
    '''
    def cards_remaining(self) -> int:
        return len(self.cards)

if __name__ == "__main__":
    d = Deck()
    d.build_deck()
    for c in d.cards:
        print(c)